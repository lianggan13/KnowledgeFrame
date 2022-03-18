## ASP.Net Core







### Data Controller-View

Keys: ViewBag、ViewData、TempData、Session

```c#
// Controller
public IActionResult Index()
{
	ViewBag.User1 = "张三";
	ViewData["User2"] = "李四";
	TempData["User3"] = "王五";
	HttpContext.Session.SetString("User4", "赵六");
	object User5 = "田七";
	return View(User5);
}

// View
@{
    ViewData["Title"] = "Index";
}
@model String
<h1>this is First Index</h1>

<h2>User1=@ViewBag.User1</h2>
<h2>User2=@ViewData["User2"]</h2>
<h2>User3=@TempData["User3"]</h2>
<h2>User4=@Context.Session.GetString("User4")</h2>
<h2>User5=@Model</h2>
```

### AOP-Filter

Keys: IResourceFilter、IAsyncResourceFilter
```c#
// 资源缓存
// IResourceFilter 执行顺序:
a.CustomResourceFilterAttribute.OnResourceExecuting 
b.控制器的构造函数 - 实例化控制器 
c.执行Action方法 
d.CustomResourceFilterAttribute.OnResourceExecuted
```

Keys: IActionFilter、IAsyncActionFilter
```c#
// Action 方法前后的日志记录
// IActionFilter 执行顺序:
a.执行控制器的构造函数 
b.执行CustomActionFilterAttribute.OnActionExecuting
c.执行Action方法 
d.CustomActionFilterAttribute.OnActionExecuted
```

Keys: IResultFilter、IAsyncResultFilter
```c#
// 结果生成前后扩展: 渲染视图和结果的时候，做结果的统一处理；JSON格式的统一处理
a.CustomResultFilterAttribute.OnResultExecuting 
b.开始渲染生成视图内容
c.CustomResultFilterAttribute.OnResultExecuted
```

Keys: IAlwaysRunResultFilter
```c#
// 响应结果的补充: 对HttpContext.Result赋值后，进行扩展补充
```

Keys: AllowAnonymousAttribute
```c#
// 响应结果的补充
```

Keys: IExceptionFilte、IAsyncExceptionFilter

```c#
// 异常处理
```

Keys: ActionFilterAttribute
```c#
// 包含了 ActionFilter 和 ResultFilter 的多种实现
public class CustomAllActionResultFilterAttribute : ActionFilterAttribute
{

	private readonly ILogger<CustomAllActionResultFilterAttribute> _ILogger;
	public CustomAllActionResultFilterAttribute(ILogger<CustomAllActionResultFilterAttribute> iLogger)
	{
		this._ILogger = iLogger;
	}


	public override void OnActionExecuting(ActionExecutingContext context)
	{
		var para = context.HttpContext.Request.QueryString.Value;
		var controllerName = context.HttpContext.GetRouteValue("controller");
		var actionName = context.HttpContext.GetRouteValue("action");
		_ILogger.LogInformation($"执行{controllerName}控制器--{actionName}方法；参数为：{para}");
	}

	public override void OnActionExecuted(ActionExecutedContext context)
	{
		var result = Newtonsoft.Json.JsonConvert.SerializeObject(context.Result);
		var controllerName = context.HttpContext.GetRouteValue("controller");
		var actionName = context.HttpContext.GetRouteValue("action");
		_ILogger.LogInformation($"执行{controllerName}控制器--{actionName}方法:执行结果为：{result}");
	}

	public override async Task OnActionExecutionAsync(ActionExecutingContext context, ActionExecutionDelegate next)
	{
		var controllerName = context.HttpContext.GetRouteValue("controller");
		var actionName = context.HttpContext.GetRouteValue("action");

		var para = context.HttpContext.Request.QueryString.Value;
		_ILogger.LogInformation($"执行{controllerName}控制器--{actionName}方法；参数为：{para}");

		ActionExecutedContext executedContext = await next.Invoke(); //这句话执行就是去执行Action  

		var result = Newtonsoft.Json.JsonConvert.SerializeObject(executedContext.Result);
		_ILogger.LogInformation($"执行{controllerName}控制器--{actionName}方法:执行结果为：{result}");
	}

	public override void OnResultExecuting(ResultExecutingContext context)
	{
		base.OnResultExecuting(context);
	}

	public override void OnResultExecuted(ResultExecutedContext context)
	{
		base.OnResultExecuted(context);
	}

	public override Task OnResultExecutionAsync(ResultExecutingContext context, ResultExecutionDelegate next)
	{
		return base.OnResultExecutionAsync(context, next);
	}
}
```






Keys: AuthorizeAttribute

```c#
// 权限验证
```










### Nancy

Keys:Get、AddUrlSegment、dynamic

```c#
// Get Request
private const string Path = "/api/position/confirm/{positionId}/{command}/{no}/{msg}";
protected override RestRequest CreateRequest()
{
    RestRequest request = base.CreateRequest();
    request.Timeout = 5000;
    request.Method = Method.GET;
    request.AddUrlSegment("positionId", positionId);
    request.AddUrlSegment("command", command);
    request.AddUrlSegment("no", no);
    request.AddUrlSegment("msg", msg);
    return request;
}

// Get Response
private Response PositionAlgorithmConfirm(dynamic parameters)
{
    int positionId = parameters.positionId;
    int no = parameters.no;
    int command = parameters.command;
    string msg = parameters.Msg;

    return ResponseData.Success(success).ToString();
}
```



Keys: Post、AddParameter、Request.Form、Request.Body、JObject

```c#
// Post Request key-value
private const string Path ="/api/position/confirm/algorithm";
protected override RestRequest CreateRequest()
{
    RestRequest request = base.CreateRequest();
    request.Timeout = 6000;
    request.Method = Method.POST;
    request.AddParameter("positionId", positionId);
    request.AddParameter("command", command);
    request.AddParameter("no", no);
    request.AddParameter("msg", msg);

    return request;
}

// Post Response key-value
private Response PosAlgorithmConfirm(dynamic _)
{
    int positionId = int.Parse(GetForm("positionId"));
    //int no = int.Parse(GetForm("no"));
    int command = int.Parse(GetForm("command"));
    string msg = GetForm("msg");
 
    return ResponseData.Success().ToString();
}

private string GetForm(string key)
{
    if (!Request.Form.ContainsKey(key))
    {
        throw new ParameterIsNullOrMissingException(key);
    }
    return Request.Form.ToDictionary()[key];
}

// Post Request json object
private const string Path = "/api/position/issue/user";
protected override RestRequest CreateRequest()
{
    RestRequest request = base.CreateRequest();
    request.Method = Method.POST;
    request.AddParameter("application/json",Newtonsoft.Json.JsonConvert.SerializeObject(obj), ParameterType.RequestBody);
    return request;
}

private const string Path = "/KeyServer/app/toolsUser/save/batch";
protected override RestRequest CreateRequest()
{
    RestRequest request = base.CreateRequest();
    request.Method = Method.POST;
    request.AddHeader("Content-Type", "application/json;charset=UTF-8");
    //toolsId
    request.AddJsonBody(toolUsers);
    return request;
}


public static ResponseData AddOrUpdateUser(User user)
{
    const string apiUrl = "api/user/upsert";
    var restClent = CreateRestClient();
    var request = new RestRequest(apiUrl, Method.POST)
    {
        //Timeout = 10 * 1000
    };
    var json = JObject.FromObject(user);
    json.Add("Photo", user.Photo);          // add Photo property
    json["NewPassword"] = user.Password;    // set NewPassword property
    request.AddParameter("application/json", json, ParameterType.RequestBody);

    var response = restClent.Execute(request);
    var responseData = JsonConvert.DeserializeObject<ResponseData>(response.Content);
    return responseData;
}

// Post Response json object
private Response PositionIssueUser(dynamic _)
{
    PositionIssueUsersParams obj = GetContent<PositionIssueUsersParams>();
    return ResponseData.Success().ToString();
}

private T GetContent<T>(Encoding encoding = Encoding.UTF8)
{
    byte[] data = new byte[Request.Body.Length];
    Request.Body.Read(data, 0, data.Length);
    var json = encoding.GetString(data);
    return Newtonsoft.Json.JsonConvert.DeserializeObject<T>(json);
}
```



### ReverseProxy

```C#
Asp.Net Core 反向代理
包: Yarp.ReverseProxy

"ReverseProxy": {
	"Routes": {
	  "InterlockRoute": {
		"ClusterId": "InterlockCluster",
		"Match": {
		  "Path": "/Interlock/{**remainder}"
		},
		"Transforms": [
		  { "PathRemovePrefix": "/Interlock" },
		  {
			"RequestHeader": "AuthKey",
			"Set": "6666666666666666"
		  }
		]
	  }
	},
	"Clusters": {
	  "InterlockCluster": {
		"Destinations": {
		  "Interlock": {
			"Address": "http://192.168.1.102:8080/"
		  }
		}
	  }
	}
},

builder.Services.AddReverseProxy()
.LoadFromConfig(builder.Configuration.GetSection("ReverseProxy"));

app.MapReverseProxy();
```





### Log4Net

```
log4Net.AspNetCore
Microsoft.Extensions.Logging.Log4Net.AspNetCore
http://logging.apache.org/log4net/release/config-examples.html
Net Core IIS下无Log4Net日志输出，命令行下却有（dotnet运行）：
https://www.cnblogs.com/liushen/p/Findout_Why_IIS_Has_Not_Log_But_Console_Has.html
```



