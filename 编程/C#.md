## C#

### C# 10.0

Keys: with、record

```c#
var parse = (string s) => int.Parse(s);
var choose = [Obsolete] object (bool b) => b ? 1 : "2";

var apples = new { Item = "Apples", Price = "1.19" };
Console.WriteLine($"original apples: {apples}");
var saleApples = apples with { Price = "0.79" };
Console.WriteLine($"sale apples: {saleApples}");

public readonly record struct Point1(double X, double Y, double Z);

public record struct Point2
{
    public double X { get; init; }
    public double Y { get; init; }
    public double Z { get; init; }
}

public record Person
{
    public string FirstName { get; set; } = default!;
    public string LastName { get; set; } = default!;
};
```



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

Keys: 获取私有属性(字段)

```c#
var pi = sender.GetType().GetProperty("VisualOffset", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
var offset = ((Vector)pi.GetValue(sender)).X;
```





#### 线程

线程安全？



 #### 内存管理

托管资源 与 非托管资源

一个对象没有任何标签（引用），c#就会被将对象从内存中进行垃圾回收

多个引用意味多个途径改变一个对象的数据 

对于***\*托管资源\****，.Net clr把所有的引用对象都分配到***\*托管堆\****上，当对象使用完后或者或没有任何引用标签指向该对象的时候，.Net clr 会将对象从内存中进行回收。

对于***\*非托管资源\****，需要进行手动释放，开发人员通常会把清理这类资源的代码写到Close、Dispose或者Finalize方法中





#### 通信

Keys: MQTT

```c#
static void InitMqttServer()
{
	mqttServer = new MQTTnet.MqttFactory().CreateMqttServer();
	mqttServer.ApplicationMessageReceivedHandler = new MqttApplicationMessageReceivedHandlerDelegate(ReceiveMessage);
	mqttServer.ClientConnectedHandler = new MqttServerClientConnectedHandlerDelegate(new Action<MqttServerClientConnectedEventArgs>(ClientConnected));

	// 地址  
	// 安全：用户名/密码
	MqttServerOptionsBuilder builder = new MqttServerOptionsBuilder();
	// 指定IP
	builder.WithDefaultEndpointBoundIPAddress(IPAddress.Parse("127.0.0.1"));
	builder.WithEncryptedEndpointPort(1883);// 端口号必须是1883，否则客户端连接不上
	builder.WithConnectionValidator(ConnectionValidator);
	IMqttServerOptions options = builder.Build();

	mqttServer.StartAsync(options).GetAwaiter().GetResult();

}

static void ConnectionValidator(MqttConnectionValidatorContext context)
{
	// 当客户端连接的时候，会触发这个委托 
	if (context.Username == "zhaoxi" && context.Password == "jovan")
	{
		context.ReasonCode = MqttConnectReasonCode.Success;
	}
	else
	{
		context.ReasonCode = MqttConnectReasonCode.BadUserNameOrPassword;
	}
}

static void ReceiveMessage(MqttApplicationMessageReceivedEventArgs e)
{
	System.Console.WriteLine("服务端接收到消息：" + e.ApplicationMessage.Payload);
}

static void ClientConnected(MqttServerClientConnectedEventArgs e)
{
	Console.WriteLine("有客户端接入：" + e.ClientId);
}

static void Connect()
{
	mqttClient = new MqttFactory().CreateManagedMqttClient();

	MqttClientOptionsBuilder mqttClientBuilder = new MqttClientOptionsBuilder();
	mqttClientBuilder.WithClientId(Guid.NewGuid().ToString());
	mqttClientBuilder.WithTcpServer("127.0.0.1", 1883);// 端口号必须是1883，否则客户端连接不上
	mqttClientBuilder.WithCredentials("zhaoxi", "jovan");
	ManagedMqttClientOptionsBuilder builder = new ManagedMqttClientOptionsBuilder();
	// 指定IP
	builder.WithClientOptions(mqttClientBuilder);
	IManagedMqttClientOptions options = builder.Build();

	mqttClient.StartAsync(options).GetAwaiter().GetResult();
}
```

Keys: WebSocket

```c#
ServerConfig serverConfig = new ServerConfig();
serverConfig.Ip = "127.0.0.1";
serverConfig.Port = 9090;

if (!webSocketServer.Setup(serverConfig))
{
	Console.WriteLine("配置信息设置异常");
	return;
}

if (!webSocketServer.Start())
{
	Console.WriteLine("开启服务器失败！");
	return;
}

Console.WriteLine("WebSocket服务正在监听....");

webSocketServer.NewSessionConnected += WebSocketServer_NewSessionConnected;
webSocketServer.NewMessageReceived += WebSocketServer_NewMessageReceived;
webSocketServer.SessionClosed += WebSocketServer_SessionClosed;

webSocket = new WebSocket("ws://127.0.0.1:9090");
webSocket.Open();
webSocket.Opened += WebSocket_Opened;
webSocket.Error += WebSocket_Error;
webSocket.MessageReceived += WebSocket_MessageReceived;
```





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

