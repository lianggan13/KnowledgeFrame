### C#

#### 类型

```c#
值类型：
    int、char、float、decimal、bool、enum、struct
引用类型：
    object、string、class、interface、Array、[]、delegate
泛型：
    public class BaseModel<T> where T:class,new()
    public static string ExtensioFunc<T>(this T t) where T:Enum
    
```



#### 反射

AbstractFactory + ConfigurationManager + string (Assembly Namespace Class)

依赖注入：通过 IOC 容器创建对象，注入对象参数（构造函数注入，属性注入，接口注入）



#### 线程

线程安全？



 #### 内存管理

托管资源 与 非托管资源

一个对象没有任何标签（引用），c#就会被将对象从内存中进行垃圾回收

多个引用意味多个途径改变一个对象的数据 

对于***\*托管资源\****，.Net clr把所有的引用对象都分配到***\*托管堆\****上，当对象使用完后或者或没有任何引用标签指向该对象的时候，.Net clr 会将对象从内存中进行回收。

对于***\*非托管资源\****，需要进行手动释放，开发人员通常会把清理这类资源的代码写到Close、Dispose或者Finalize方法中





#### 面试

关键点：专业能力(技术、处理问题)、语言表达能力(逻辑、论点，论据、论证，推论)

问题：

> + 很多Service 部署到一台服务器上，如何应对产生争抢资源的现象？
>
> 	合理分配服务，避免资源竞争。如：将No-sql redis 分布式缓存 与主SQLSERVER数据库分开；Web 主站点与升级服务 以及图片服务 分离，因为它们非常消耗带宽。
>
> + 一台（单台）服务器的线程数是有限的，链接数是有限的，如何进行分流处理？
>
> 	应用集群方案NLB，完成请求分发，不同机器轮询处理请求，把压力分布到不同机器上，解决单台服务器处理有限的情景。
>
> 	 + 高并发数据库访问，如何处理读写死锁？如何实现高性能高并发插入、查询？
>
> 	数据库集群读写分离，把插入的主库全部用来插入操作，大部分的读操作去从库读取。
>
> 	产生死锁的情况大大降低。使用基于内存的数据库No-sql，如 MongoDB,redis，完成高性能高并发插入、查询。
>
> + 分布式服务器如何共享缓存数据，用户状态，同步不同机器之间数据同步的问题？
>
> 	使用Memcache分布式缓存，但缺乏持久化和容灾能力，所以改用 redis。

