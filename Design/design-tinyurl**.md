# Design TinyURL
## S场景： 
    * 长到短
    * 短到长
## N需求：  
    * **qps**：日活100M   每人每天：写(长到短)0.1   读(短到长)1   -->  qps: 写100 读1k   peak qps：写200 读2k   -->   千级别的qps可以单台SSD MySQL搞定
    * 存储：每天新产生10M个长链接<-->短链接映射  平均每个大小100B   每天1GB  --> 1TB的硬盘可以用3年  -->  一般来说存储不成问题
## A服务与接口：
    * URLService：Core(Business Logic)层：类URLService  接口 URLService.encode(String longUrl)   &  URLService.decode(String short_url)
    * Web层： REST API：
        * GET:/{short_url}  返回一个http redirect response(301)
        * POST:  goo.gl做法： POST: https://goo.gl/api/shortenbit.ly做法： POST: https://bitly.com/data/shorten  Request Body: {url=long_url}  返回OK(200), data里带生成的short_url
## K数据存取
    * select 选存储结构  -->  内存 or 文件系统 or 数据库  --> SQL or NoSQL?
        * SQL vs NoSQL?
            * 是否需要支持Transaction？  --> NoSQL不支持Transaction
            * 是否需要丰富的SQL Query？ --> NoSQL丰富度不如SQL
            * 是否需要AUTO_INCREMENT ID？ -->  NoSQL 只能做到全局unique的Object_id
            * 对QPS的要求？ -->  NoSQL性能高 比如Memcached的qps可以达到million级别  MongoDB可以达到10k级别  MySQL只能在K这个级别
            * 对Scalability的要求多高？  --> SQL需要程序员自己写代码来scale  NoSQL自带(sharding, replica)
    * schema细化数据表
        * 一个表：两列(id, long_url)  其中id为主键(自带index)   long_url也index  这样一张表可以方便双向查
## 算法
    * Solution1: hash function: 把long_url用md5/sha1哈希(md5把一个string转化成128位二进制数 一般用32位16进制表示，sha1则用40位十六进制表示)。
                 这两个算法都可以保证哈希值分布很随机 但冲突是不可避免的。事实上任何一个hash算法都不可避免有冲突。 
                 但优点是很简单，可以直接取hash结果的前n(比如说6)位。  
                 解决冲突的方案：用(long_url + timestamp) 来哈希  如果冲突的话重试(重试时timestamp会变，会生成新的hash)  
                 但是这种方法的问题也很明显：流量不多时可行，但当url多时会产生大量冲突，效率很低。
    * Solution2: base62: 把6位的short_url看成一个62进制数(0-9, a-z, A-Z)，可以表示 62 ^ 6 = 570亿个数字 
                 (整个互联网的网页数在trillion级别，即一亿万级别，6位足够)   
                 每个short_url对应一个十进制整数  这个整数就可以是数据库中的auto_increment_id。
## E优化
    * 如何提高响应速度？
        * 提高web server 和数据库之间的响应速度： 
          利用memcached 提高响应速度(即利用cache)  cache没命中才去数据库搜  把90%的读请求都引流到cache上
        * 提高web server和浏览器之间的响应速度：
          不同地区使用不同的web server和缓存server  所有地区share一个db 用于缓存没hit的情况  提高DNS解析把不同地区的用户match到最近的web server
    * 如果一台MySQL存不下 or 忙不过来？  
        可能面临的问题：cache资源不够   写操作越来越多   cache miss率变高
        * 拆数据库：通常有两种方式 1. 把不同表放到不同机器(vertical sharding)；2.把数据散列到不同的机器(horizontal sharding)   那显然我们这里要用第二种方法  最简单的方法是按id取模 hash到不同机器 那问题来了：如何在多台机器间共享一个全局自增id？ 可行的solution有：1. 开一台新的机器专门维护这个全局自增id；2. 用zk。  这两种方法都不好，业内的做法是 把sharding_key作为第一位直接放到short_url，这样就只需要每台机器自增即可。
            * 具体做法：
            long_url -> hash(long_url) % 62 找到对应机器 -> 在这台机器生成short_url -> 返回short_url;    
            short_url -> 提取第一位得到sharding key 找到指定机器 -> 返回long_url    
            新增一台机器 ->  找原来机器里负责range(0-61)最大的机器 -> 将其range减半 -> 把一半放到新增机器上
            新增一个新功能custom url怎么做？：单独建一张表，先从custom表查，再从url表查。 注意千万不要在url表里插一列custom 这会使得这列大部分值为空。