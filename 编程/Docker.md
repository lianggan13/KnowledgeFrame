## Docker

**菜鸟教程 https://www.runoob.com/docker/docker-dockerfile.html**

![微服务架构图](Images\MicroServices.png)

### Ubuntu

```c#
1.更新源
sudo apt update

2.安装必要的依赖软件
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

3.导入源仓库的 GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

4.将 Docker apt 软件源添加到系统
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

5.添加完成后再次更新 apt 源
sudo apt update

6.开始安装docker
sudo apt install docker-ce docker-ce-cli containerd.io

7.查看是否安装成功
sudo docker --version

8.设置Docker开机自启
sudo systemctl enable docker

9.设置 DNS
sudo vi /etc/default/docker
     DOCKER_OPTS="--dns 8.8.8.8"
   
10.重启
sudo service docker stop
sudo service docker start
```



### Command

```c#
docker pull <image name>  // 拉取镜像 如: microsoft/mssql-server-linux (SQL server)
docker run hello-world
docker run -d -p 80:80 docker/getting-started
docker images // 查看镜像
docker container list // 查看容器
docker ps // 运行中的容器
docker ps -a // 所有容器状态
docker stop <container name>
docker start <container name>
docker restart <container name>
docker update --restart=always <container name> // 容器自启动
docker rm <container name> // 删除容器(删除前需要先停止容器)
docker rm -f <container name> // 强制删除容器
docker rmi <image name> // 删除镜像
docker stop $(docker ps -q) & docker rm $(docker ps -aq) // 停用并删除全部容器

docker exec -it <container id> /bin/bash # 进入容器内部
docker exec -it <container name> bash # 进入容器内部
	   > exit # 退出容器
// 构建镜像
docker build -t <image name> -f <PATH: dockfile> <PATH: context>
ex: docker build -t webapp -f ./ASIS/ASIS.Server/Dockerfile ./

// 运行容器
docker run -p 8009:80 --name <container name> <image name>
ex: docker run -p 8009:80 --name webappinstance webapp
    docker run -itd -p 8009:80 --name webappinstance webapp
    
x docker run -p 8000:80 -e "ASPNETCORE_URLS=http://+:80" -it --rm microsoft/dotnet
x docker run -p 8000:80 -e "ASPNETCORE_URLS=http://+:80" -it --rm mcr.microsoft.com/dotnet/sdk:2.0
```



### Docker-Compose



### Docker-Swarm



### Docker-Hub

### Consul

![](Images\Consul.png)

服务注册发现

Keys: start

```
docker pull consul
docker run -itd -p 8500:8500 --name consulinstance1 consul http://192.168.3.230:8500
docker rm -f consulinstance1
```

Keys: Nuget: Consul

```c#
public static void RegisterConsul(this IConfiguration configuration)
{
	ConsulClient client = new ConsulClient(c =>
	{
		c.Address = new Uri("http://localhost:8500/");
		c.Datacenter = "dc1";
	});

	string ip = string.IsNullOrWhiteSpace(configuration["ip"]) ? "192.168.3.230" : configuration["ip"];
	int port = int.Parse(configuration["port"]);//命令行参数必须传入
	int weight = string.IsNullOrWhiteSpace(configuration["weight"]) ? 1 : int.Parse(configuration["weight"]);

	client.Agent.ServiceRegister(new AgentServiceRegistration()
	{
		ID = "service" + Guid.NewGuid(),//唯一的人---C罗---独一无二
		Name = "ZhaoxiService",//组名称-Group   尤文图斯
		Address = ip,//其实应该写ip地址--身高
		Port = port,//不同实例--体重
		Tags = new string[] { weight.ToString() },//标签
		Check = new AgentServiceCheck()
		{
			Interval = TimeSpan.FromSeconds(12),//间隔12s一次
			HTTP = $"http://{ip}:{port}/Api/Health/Index",
			Timeout = TimeSpan.FromSeconds(5),//检测等待时间
			DeregisterCriticalServiceAfter = TimeSpan.FromSeconds(20)//失败后多久移除
		}
	});
	//命令行参数获取
	Console.WriteLine($"{ip}:{port}--weight:{weight}");
}

public void RequestConsul()
{
	ConsulClient client = new ConsulClient(c =>
	{
		c.Address = new Uri("http://192.168.3.230:8500/");
		c.Datacenter = "dc1";
	});
	var response = client.Agent.Services().Result.Response;
	//有了consul 程序需要知道哪些信息，才能调用服务？---哪一组服务--哪个球队
	string url = null;
	url = "http://ZhaoxiService/api/users/all";//consul提供的是ip+port

	Uri uri = new Uri(url);
	string groupName = uri.Host;
	AgentService agentService = null;

	var serviceDictionary = response.Where(s => s.Value.Service.Equals(groupName, StringComparison.OrdinalIgnoreCase)).ToArray();//找到的全部服务--4个
	{
		agentService = serviceDictionary[0].Value;//直接拿的第一个
		//这里有三个服务或者服务实例，只需要选择一个调用，那么这个选择的方案，就叫 负载均衡策略
	}
	//{
	//    //轮询策略 也是平均，但是太僵硬了
	//    agentService = serviceDictionary[iIndex++ % serviceDictionary.Length].Value;
	//}
	//{
	//    //平均策略--随机获取索引--相对就平均
	//    agentService = serviceDictionary[new Random(iIndex++).Next(0, serviceDictionary.Length)].Value;
	//}
	//{
	//    //权重策略--能给不同的实例分配不同的压力---注册时提供权重
	//    List<KeyValuePair<string, AgentService>> pairsList = new List<KeyValuePair<string, AgentService>>();
	//    foreach (var pair in serviceDictionary)
	//    {
	//        int count = int.Parse(pair.Value.Tags?[0]);//1   5   10
	//        for (int i = 0; i < count; i++)
	//        {
	//            pairsList.Add(pair);
	//        }
	//    }
	//    //16个  
	//    agentService = pairsList.ToArray()[new Random(iIndex++).Next(0, pairsList.Count())].Value;
	//}
	url = $"{uri.Scheme}://{agentService.Address}:{agentService.Port}{uri.PathAndQuery}";
	string content = InvokeApi(url);
	base.ViewBag.Users = Newtonsoft.Json.JsonConvert.DeserializeObject<IEnumerable<User>>(content);
	Console.WriteLine($"This is {url} Invoke");
}

public string InvokeApi(string url)
{
	using (HttpClient httpClient = new HttpClient())
	{
		HttpRequestMessage message = new HttpRequestMessage();
		message.Method = HttpMethod.Get;
		message.RequestUri = new Uri(url);
		var result = httpClient.SendAsync(message).Result;
		string content = result.Content.ReadAsStringAsync().Result;
		return content;
	}
}
```

### Polly

![](Images\Polly.png)

Polly是一种.NET弹性和瞬态故障处理库，允许我们以非常顺畅和线程安全的方式来执诸如行重试，断路，超时，故障恢复等策略。

### Skywalking

![](Images\Skywalking.png)

分布式追踪和APM的Server端，它将包含Collector，Storage，独立的Web UI，并使用Open Tracing规范来设计追踪数据。

### Exceptionless & ELK

![](Images\Exceptionless.png)

Exceptionless：开源的日志收集和分析框架，能为应用程序提供实时错误、特性和日志报告。

![](Images\ELK.png)

ELK：最强的分布式日志解决方案

### Apollo

![](Images\Apollo.png)

配置管理平台，能够集中化管理应用不同环境、不同集群的配置，配置修改后能够实时推送到应用端，并且具备规范的权限、流程治理等特性。





