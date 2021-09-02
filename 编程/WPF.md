### WPF

### xmlns:x

Keys：x:Array

```xaml
<x:Array x:Key="Legends" Type="{x:Type model:LegendModel}">
    <model:LegendModel
                       Name="30°"
                       IsChecked="False"
                       LegendBrush="Blue" />
    <model:LegendModel
                       Name="50°"
                       IsChecked="False"
                       LegendBrush="Green" />
    <model:LegendModel
                       Name="120°"
                       IsChecked="True"
                       LegendBrush="Red" />
</x:Array>
```





### MVVM Foundation

![](Images\mvvm_foundation_frame.PNG)

> + Messenger：View和ViewModel 以及 ViewModel和ViewModel 之间的消息通知和接收
> + ObservableObject：等价于ViewModelBase，被ViewModel继承，调用完成后立即释放，防止内存泄漏
> + PropertyObserver：封装INotifyPropertyChanged.PropertyChanged，通过其对某个对象的属性变更注册回调函数，当属性变更时触发回调函数
> + RelayCommand：封装Command，包括execution执行逻辑等



### Binding

> Bind Mode
>
> ​	 One Way:            UI <---- Model (UI Get)
>
> ​	One Way to Source:   UI ----> Model (UI Set)
>
> ​	Default(Two Way):    UI <---> Model (UI Get & Set)

+ Binding Static Class

```xaml

Title="{Binding Source={x:Static g:GlobalConfig.Version}, StringFormat='{}MaxSign Auto {0}'}"

public static class GlobalConfig
{
	 public static string Version = "V1.7.0";
}


xmlns:com="clr-namespace:GTS.MaxSign.Controls.Assets.Components"
<Popup Opened="{DXEvent Handler='$com:PopupFocusHelper.Popup_Opened(@sender,@args)'}"/>

namespace GTS.MaxSign.Controls.Assets.Components
{
    public static class PopupFocusHelper
    {
        public static void Popup_Opened(object sender, System.EventArgs e)
        {
            Popup popup = sender as Popup;
            IntPtr handle = GetHwnd(popup);
            SetFocus(handle);
        }

        [DllImport("User32.dll")]
        public static extern IntPtr SetFocus(IntPtr hWnd);

        public static IntPtr GetHwnd(Popup popup)
        {
            HwndSource source = (HwndSource)PresentationSource.FromVisual(popup.Child);
            return source.Handle;
        }
    }
}
```

+ DxBinding

```xaml
@s, @Self
@p, @TemplatedParent
@e, @ElementName
@r, @StaticResource
@a, @FindAncestor
@c, @DataContext
@v, @value
@Reference
$int, $double, ..., $string, $object, $bool

<TextBlock Text="{DXBinding '@s.PropA'}"/>
<TextBlock Text="{DXBinding '@Self.PropA'}"/>

<TextBlock Text="{DXBinding '@e(bt).PropA'}"/>
<TextBlock Text="{DXBinding '@e(myButton).Content'}"/>
<Button Click="{DXEvent '@e(checkBox).IsChecked=true'}"/>
<TextBlock Text="{DXBinding '@ElementName(bt).PropA'}"/>
Legend="{DXBinding '@e(lbLegendMode).SelectedItem.Tag != $local:LegendMode.Common ? @e(defaultPaneLegend) : null'}"
RisingBarBrush="{DXBinding '@e(lbDataType).SelectedIndex == 0 ? `#DA5859` : null'}"

<TextBlock Text="{DXBinding '@r(resource)'}"/>
<TextBlock Text="{DXBinding '@StaticResource(resource)'}"/>

<TextBlock Text="{DXBinding '@a($Window).Title'}"/>
<TextBlock Text="{DXBinding '@a($Window, 1).Title'}"/>
<TextBlock Text="{DXBinding '@a($ComboBox).Text',Mode=OneTime}" />
<TextBlock Text="{DXBinding '@FindAncestor($Window).Title'}"/>
<TextBlock Text="{DXBinding '@FindAncestor($Window, 1).Title'}"/>
<TextBlock Text="Text" Visibility="{DXBinding $Visibility.Hidden}"/>
<TextBlock Text="{DXBinding 'typeof($int)'}"/>
<TextBlock Text="{DXBinding 'typeof($Window)'}"/>
<TextBlock Text="{DXBinding 'typeof($dx:DXWindow)'}"/>
<TextBlock Text="{DXBinding '(PropertyA as $dx:DXWindow).CurrentWindow'}"/>

<TextBlock Text="{DXBinding '@c'}"/>
<TextBlock Text="{DXBinding '@c.PropA'}"/>
<TextBlock Text="{DXBinding '@DataContext'}"/>
<TextBlock Text="{DXBinding '@DataContext.PropA'}"/>
MinLimit="{DXBinding @c.OptimalTemperature + 10, Mode=OneTime}"
IsEnabled="{DXBinding '!@c.AutoGrid'}" />
DisplayFormatString="{DXBinding '`0 `+@c.GridAlignment.ToString().ToLower() + `(s)`'}" />
IsEnabled="{DXBinding '@c.WorkTimeOptionsEnabled and @c.WorkTimeOnly'}"


<TextBlock Text="{DXBinding '@Reference(bt).Content'}"/>

<TextBlock Text="{DXBinding '$Application.Current.FindResource(`trans0471`).ToString()'}"/>
<TextBlock Text="{DXBinding Expr='!$string.IsNullOrEmpty(LogTypeText) ?LogTypeText:$Application.Current.FindResource(`trans0471`)',BackExpr='@v'}"/>

<TextBlock Text="{DXBinding '(double)1'}"/>
<TextBlock Text="{DXBinding 'Customer.FirstName + ` ` + Customer.LastName'}"/>

<TextBlock Text="{DXBinding '2+2'}"/>
<TextBlock Text="{DXBinding 'Calculate()'}"/>
<TextBlock Text="{DXBinding 'PropA+PropB'}"/>
<TextBlock Text="{DXBinding 'Calculate(PropB)'}"/>
<TextBlock Text="{DXBinding 'PropA.PropB.Calculate().PropC'}"/>
<TextBlock Text="{DXBinding 'Calculate(PropA, PropB.Prop1 + 2).PropC'}"/>



<Control IsEnabled="{DXBinding Expr='!IsDisabled', BackExpr='!@v'}"/>
<TextBox Text="{DXBinding '!PropA', BackExpr='PropA=!@v'}"/>
<TextBlock Visibility="{DXBinding EnableBand?`Visible`:`Collapsed`}">
<TextBlock Visibility="{DXBinding 'TestTasks.Count>0?`Collapsed`:`Visible`'}" />
<TextBlock Tag="{DXBinding 'PropA+2', BackExpr='$int.Parse(@v)-2', Mode=TwoWay}"/>
<TextBlock Text="{DXBinding '!PropA', BackExpr='!$bool.Parse(@value)', Mode=TwoWay}"/>
<Control Visibility="{DXBinding Expr='IsVisible ? `Visible` : `Collapsed`', BackExpr='@v == $Visibility.Visible'}"/>
<RadioButton IsChecked="{DXBinding Expr='MainContent.GetType() == typeof($local:TestSysView)', BackExpr='true'}" />
<TextBox Text="{DXBinding 'FirstName + ` ` + LastName', BackExpr='FirstName=@v.Split(` `[0])[0]; LastName=@v.Split(` `[0])[1]'}"/>
<CheckBox Visibility="{DXBinding '( (@e(btnSkip).IsChecked)  &amp;&amp; (@e(btnSkip).Visibility == $Visibility.Visible))?`Visible`:`Collapsed`'}" />


DataSource="{DXBinding 'new $local:WebSitePerformanceIndicator().Data'}"
DataSource="{DXBinding '$local:RealEstateData.GetAnnualData()'}"
public static class RealEstateData
{
	public static List<RealEstateDataAnnualPoint> GetAnnualData()
	{
		...
	}
}
```

+ DxEvent

```xaml
<StackPanel>
    <StackPanel.DataContext>
        <local:ViewModel />
    </StackPanel.DataContext>
    <Button Content="OK" Loaded="{DXEvent Handler='Initialize()'}" />
    <Button Content="OK" Loaded="{DXEvent Handler='Initialize(); Load()'}" />
</StackPanel>

<Button Content="OK" Loaded="{DXEvent Handler='Initialize(@sender.Content, @args, @e(tb).Text)'}"/>

<Button Click="{DXEvent '@e(checkBox).IsChecked=true'}"/>

<Border  MouseDown="{DXEvent Handler=@a($UserControl).DataContext.Legend_MouseDown(@s.DataContext)}">
 
<ContextMenu x:Key="DutMenu" DataContext="{DXBinding @a($TreeView).DataContext}">
	<MenuItem Click="{DXEvent Handler='AddDutProject(@a($ContextMenu).PlacementTarget)'}" Header="{DynamicResource trans0437}" />
	<MenuItem Click="{DXEvent Handler='AddDutModel(@a($ContextMenu).PlacementTarget)'}" Header="{DynamicResource trans0438}" />
	<MenuItem
		Click="{DXEvent Handler='DeleteDut(@a($ContextMenu).PlacementTarget)'}"
		Header="{DynamicResource trans0013}"
		IsEnabled="{DXBinding '(@a($ContextMenu).PlacementTarget.DataContext.Name !=`Default Program`) &amp;&amp; (@a($ContextMenu).PlacementTarget.DataContext.Name !=`Default Model`)'}" />
	<MenuItem
		Click="{DXEvent Handler='RenameDut(@a($ContextMenu).PlacementTarget)'}"
		Header="{DynamicResource trans0016}"
		IsEnabled="{DXBinding '(@a($ContextMenu).PlacementTarget.DataContext.Name !=`Default Program`) &amp;&amp; (@a($ContextMenu).PlacementTarget.DataContext.Name !=`Default Model`)'}" />
</ContextMenu>
```



### Triggers

Description：通过指定属性的变化或者事件的触发时，更改控件的外观和行为，并且并触发器监测的属性必然为依赖属性，事件必然为路由事件

Keys：Property Trigger、Binding DataTrigger、ControlTemplate.Triggers、MultiDataTrigger、EventTrigger(RouteEvent、Actions、Storyboard)、EventSetter

#### Trigger/MultiTrigger

```xaml
// Trigger/MultiTrigger(属性触发器)
<Style x:Key="ButtonStyle" TargetType="{x:Type Button}">
    <Style.Triggers>
        <Trigger Property="IsPressed" Value="True">
            <Setter Property="Opacity" Value="0.5" />
        </Trigger>
        <Trigger Property="IsEnabled" Value="False">
            <Setter Property="Foreground" Value="Red" />
        </Trigger>
    </Style.Triggers>
</Style>

<Style x:Key="MulitTriggerButtonStyle" TargetType="Button">
    <Style.Triggers>
        <MultiTrigger>
            <MultiTrigger.Conditions>
                <Condition Property="IsPressed" Value="True" />
                <Condition Property="Background" Value="BlanchedAlmond" />
            </MultiTrigger.Conditions>
            <MultiTrigger.Setters>
                <Setter Property="Foreground" Value="Blue" />
                <Setter Property="BorderThickness" Value="5" />
                <Setter Property="BorderBrush" Value="Blue" />
            </MultiTrigger.Setters>
        </MultiTrigger>
    </Style.Triggers>
</Style>
```

#### DataTrigger/MultiDataTrigger

```xaml
// DataTrigger/MultiDataTrigger(数据触发器)
<DataTemplate.Triggers>
    <DataTrigger Binding="{Binding Path=Picture}" Value="{x:Null}">
        <Setter TargetName="viewImage" Property="Source" Value="/Images/noImage.png"/>
        ……
    </DataTrigger>
</DataTemplate.Triggers>

<DataTemplate.Triggers>
    <MultiDataTrigger>
        <MultiDataTrigger.Conditions>
            <Condition Binding="{Binding Path=Picture}" Value="{x:Null}" />
            <Condition Binding="{Binding Path=Title}" Value="Waterfall" />
        </MultiDataTrigger.Conditions>
        <MultiDataTrigger.Setters>
           <Setter TargetName="viewImage" Property="Source" Value="/Images/noImage.png"/>
           <Setter TargetName="viewImage" Property="Opacity" Value="0.5" />
           <Setter TargetName="viewText" Property="Background" Value="Brown" />
        </MultiDataTrigger.Setters>
    </MultiDataTrigger>
</DataTemplate.Triggers> 
```

#### EventTrigger

```xaml
// EventTrigger(事件触发器)
<Border  …>
    <Border.Triggers>
        <EventTrigger RoutedEvent="Mouse.MouseEnter">
            <BeginStoryboard>
                <Storyboard>
                    <ColorAnimation Duration="0:0:1" Storyboard.TargetName="MyBorder" 
                                    Storyboard.TargetProperty="Color" To="Gray" />
                </Storyboard>
            </BeginStoryboard>
        </EventTrigger>
    </Border.Triggers>
</Border>
```



### Tree

keys: VisualTree、LogicalTree

```c#
 public static List<T> GetChildObjects<T>(DependencyObject obj, Type typename) where T : FrameworkElement
        {
            DependencyObject child = null;
            List<T> childList = new List<T>();

            for (int i = 0; i <= VisualTreeHelper.GetChildrenCount(obj) - 1; i++)
            {
                child = VisualTreeHelper.GetChild(obj, i);

                if (child is T && (((T)child).GetType() == typename))
                {
                    childList.Add((T)child);
                }
                childList.AddRange(GetChildObjects<T>(child, typename));
            }
            return childList;
        }

        public static List<T> GetLogicChildObjects<T>(DependencyObject obj, Type typename) where T : FrameworkElement
        {
            List<T> childList = new List<T>();
            foreach (var child in LogicalTreeHelper.GetChildren(obj))
            {
                if (child is DependencyObject)
                {
                    if (child is T && (((T)child).GetType() == typename))
                    {
                        childList.Add((T)child);
                    }
                    childList.AddRange(GetLogicChildObjects<T>(child as DependencyObject, typename));
                }
            }

            return childList;
}
```

```c#
 ControlHelper.GetLogicChildObjects<ComboBox>(this, typeof(ComboBox))?.ForEach(t =>
            {
                t.DropDownClosed -= ComboBox_DropDownClosed2;
                t.DropDownClosed += ComboBox_DropDownClosed2;
                t.DropDownOpened -= ComboBox_DropDownOpened;
                t.DropDownOpened += ComboBox_DropDownOpened;
            });

            ControlHelper.GetLogicFisrtChildObject<TreeView>(this, typeof(TreeView))?.ForEach(t =>
            {
                t.PreviewMouseWheel -= TreeView_PreviewMouseWheel;
                t.PreviewMouseWheel += TreeView_PreviewMouseWheel;
            });
```





### VisualStateManager

> 1. VisualState: 视图状态(Visual States)表示控件在一个特殊的逻辑状态下的样式、外观；
> 2. VisualStateGroup: 状态组由**相互排斥**的状态组成，状态组与状态组并不互斥；
> 3. VisualTransition: 视图转变 (Visual Transitions) 代表控件从一个视图状态向另一个**状态转换**时的**过渡**；
> 4. VisualStateManager: 由它负责在代码中来切换到不同的状态；

<img src="Images\visual_state_manager.PNG" style="zoom: 67%;" />

```xaml
<VisualStateManager.VisualStateGroups>
    <VisualStateGroup x:Name="CommonStates">
        <VisualStateGroup.Transitions>
            <VisualTransition GeneratedDuration="0:0:1" To="MouseOver" />
            <VisualTransition GeneratedDuration="0:0:1" To="Pressed" />
            <VisualTransition GeneratedDuration="0:0:1" To="Normal" />
        </VisualStateGroup.Transitions>
        <VisualState x:Name="Normal" />
        <VisualState x:Name="MouseOver">
            <Storyboard>
                <ColorAnimation
                                Storyboard.TargetName="BackgroundBorder"
                                Storyboard.TargetProperty="Background.(SolidColorBrush.Color)"
                                To="#A1D6FC"
                                Duration="0" />
            </Storyboard>
        </VisualState>
        <VisualState x:Name="Pressed">
            <Storyboard>
                <ColorAnimation
                                Storyboard.TargetName="BackgroundBorder"
                                Storyboard.TargetProperty="Background.(SolidColorBrush.Color)"
                                To="#FCA1A1"
                                Duration="0" />
            </Storyboard>
        </VisualState>
    </VisualStateGroup>
</VisualStateManager.VisualStateGroups>
```



### Animation

Keys：BeginStoryboard、Storyboard、Storyboard.TargetName、Storyboard.TargetProperty、Duration、To、By

> + LinearAnimation
> + KeyFrameAnimation
> + PathAnimation

```xaml
Storyboard
	AutoReverse="True"
	RepeatBehavior="Forever"
	Storyboard.TargetName="[Element.Name]"
	Storyboard.TargetProperty="[Element.Property]"
	To="[Color]" To="[double]"
	Duration="[TimeLine]" />

LinearAnimation
	ColorAnimation
	PointAnimation
	DoubleAnimation
	ThicknessAnimation

KeyFrameAnimation
	DoubleAnimationUsingKeyFrames
		<LinearDoubleKeyFrame KeyTime="0:0:0" Value="180" />
		<DiscreteDoubleKeyFrame  KeyTime="0:0:0.5" Value="180"/>
		<DiscreteDoubleKeyFrame  KeyTime="0:0:1" Value="100"/>
		<SplineDoubleKeyFrame  KeySpline="1,0 0.5,1" KeyTime="0:0:1" Value="200" />
	ColorAnimationUsingKeyFrames
		<DiscreteColorKeyFrame KeyTime="0:0:0.5" Value="Red" />
		<DiscreteColorKeyFrame KeyTime="0:0:1" Value="Orange" />

PathAnimation
	PointAnimationUsingPath
	DoubleAnimationUsingPath


// RadioButton --> RoutEvent:Check、UnCheck --> EventTrigger --> BeginStoryboard --> Storyboard --> DoubleAnimation --> Border

<Storyboard x:Key="UserInfoStoryboard">
	<DoubleAnimation Duration="0:0:0.2" To="0"
					 Storyboard.TargetName="tt"
					 Storyboard.TargetProperty="X"/>
</Storyboard>

<Storyboard x:Key="CloseUserInfoStoryboard">
	<DoubleAnimation Duration="0:0:0.1"
					 Storyboard.TargetName="tt"
					 Storyboard.TargetProperty="X"/>
</Storyboard>

<Window.Triggers>
	<EventTrigger RoutedEvent="Button.Click" SourceName="btnUsreInfo">
		<BeginStoryboard Storyboard="{StaticResource UserInfoStoryboard}"/>
	</EventTrigger>
	<EventTrigger RoutedEvent="Button.Click" SourceName="btnCloseUserInfo">
		<BeginStoryboard Storyboard="{StaticResource CloseUserInfoStoryboard}"/>
	</EventTrigger>
</Window.Triggers>

<RadioButton x:Name="usrRadBtn" />
<Border>
	<Border.RenderTransform>
		<TranslateTransform X="250" x:Name="tt"/>
	</Border.RenderTransform>
</Border>
```



### Command

Keys：Command、CommandParameter、EventTrigger、CallMethodAction、InvokeCommandAction

~~~xaml
1.通过 事件 
<Button Click="Button_Click"></Button>
2.通过 命令
<Button Command="{Binding Path=DataContext.OprateDataGridRow, RelativeSource={RelativeSource Mode=FindAncestor,AncestorType={x:Type UserControl}}}"
        CommandParameter="{Binding RelativeSource={x:Static RelativeSource.Self}}">
</Button>	//  RelativeSource.Self     Button 自身作为参数
3.通过 事件触发器 
xmlns:Interaction="http://schemas.microsoft.com/expression/2010/interactions"
xmlns:Interactivity="http://schemas.microsoft.com/expression/2010/interactivity"
<Button>
    <Interactivity:Interaction.Triggers>
        <Interactivity:EventTrigger EventName="Click">
            <Interaction:CallMethodAction TargetObject="{Binding Path=DataContext,RelativeSource={RelativeSource Mode=FindAncestor,AncestorType={x:Type UserControl}}}" 
                                          MethodName="Button_Click"/>
            // <Interactivity:InvokeCommandAction Command="{Binding CmbBandSelectionChanged}"/>
        </Interactivity:EventTrigger>
    </Interactivity:Interaction.Triggers>
</Button>
~~~

​	


### Presenter

Keys：ContentPresenter、ItemsPresenter

```xaml
<ContentControl Content="Content..." ContentStringFormat="This is {0} !">
    <ContentControl.Template>
        <ControlTemplate TargetType="ContentControl">
            <Border BorderBrush="Blue" BorderThickness="1">
                <ContentPresenter />
                <!--<ContentPresenter Content="{TemplateBinding Content}" />-->
            </Border>
        </ControlTemplate>
    </ContentControl.Template>
</ContentControl>

<TreeView.Template>
    <ControlTemplate TargetType="{x:Type TreeView}">
        <Border BorderBrush="Red" BorderThickness="1">
            <ItemsPresenter />
        </Border>
    </ControlTemplate>
</TreeView.Template>
```






### Template

#### ControlTemplate	

Keys：ListViewItem、ControlTemplate.Triggers、TargetName

~~~xaml
<Style x:Key="ItemContStyle" TargetType="ListViewItem">
	<Setter Property="Template">
		<Setter.Value>
			<ControlTemplate TargetType="{x:Type ListViewItem}">
				<Border Name="BD_Collector">
					<TextBlock Text="{Binding Name}" Margin="20,0,0,0"
							   VerticalAlignment="Center" FontSize="12" />
				</Border>
				<ControlTemplate.Triggers>
					<Trigger Property="IsMouseOver" Value="True">
						<Setter TargetName="BD_Collector" Property="Background" Value="#f1f1f1" />
					</Trigger>
					<Trigger Property="IsSelected" Value="True">
						<Setter TargetName="BD_Collector" Property="Background" Value="#376BFA" />
						<Setter Property="Foreground" Value="White" />
						<Setter Property="BorderBrush" Value="White" />
					</Trigger>
				</ControlTemplate.Triggers>
			</ControlTemplate>
		</Setter.Value>
	</Setter>
</Style>

<Button>
	<Button.Template>
		<ControlTemplate TargetType="{x:Type Button}">
			<Border x:Name="border" Background="{TemplateBinding Background}">
				<Image
					x:Name="imgBtn"
					Cursor="Hand"
					Source="/Resource/images/basis_normal.png" />
			</Border>
			<ControlTemplate.Triggers>
				<Trigger Property="IsMouseOver" Value="True">
					<Setter Property="Background" Value="#394867" />
					<Setter TargetName="imgBtn" Property="Source" Value="/Resource/images/basis_hover.png" />
				</Trigger>
			</ControlTemplate.Triggers>
		</ControlTemplate>
	</Button.Template>
</Button>
~~~

- Keys：ItemContainerStyle、ListBoxItem

~~~xaml
<dxe:ListBoxEdit.ItemContainerStyle>
	<Style TargetType="ListBoxItem">
		<Style.Triggers>
			<Trigger Property="IsSelected" Value="True">
				<Setter Property="Background" Value="Transparent"/>
			</Trigger>
		</Style.Triggers>
	</Style>
</dxe:ListBoxEdit.ItemContainerStyle>
~~~

- Keys：ContentPresenter

~~~xaml
<ControlTemplate x:Key="HeaderTemplate" TargetType="{x:Type Label}">
	<Canvas Background="#C40D42" >
		<Image Height="56" Canvas.Left="0" Canvas.Top="0" Stretch="UniformToFill" Source=".\Images\Banner.png"/>
		<ContentPresenter Canvas.Right="10" Canvas.Top="25" Content="{TemplateBinding Content}" />
	</Canvas>
</ControlTemplate>
<Style x:Key="HeaderLabelStyle" TargetType="Label">
	<Setter Property="Template" Value="{StaticResource HeaderTemplate}" />
	<Setter Property="FontFamily" Value="Times New Roman" />
	<Setter Property="FontSize" Value="24" />
	<Setter Property="FontWeight" Value="Bold" />
	<Setter Property="Foreground" Value="#FFF7EFEF" />
</Style>
~~~



#### DataTemplate

- Keys：ItemTemplate、DataTemplate.Triggers、TargetName

```xaml
<dxe:ListBoxEdit.ItemTemplate>
	<DataTemplate>
		<StackPanel x:Name="pal">
			<CheckBox x:Name="chk" IsChecked="{Binding IsChecked}" />
		</StackPanel>
		<DataTemplate.Triggers>
			<DataTrigger Binding="{Binding ElementName=chk, Path=IsChecked}" Value="true">
				<Setter TargetName="pal" Property="Background" Value="#EEF7FF" />
			</DataTrigger>
		</DataTemplate.Triggers>
	</DataTemplate>
</dxe:ListBoxEdit.ItemTemplate>
```

### Data Validation

- Keys：Validation.ErrorTemplate、ValidatesOnExceptions、ValidatesOnDataErrors、NotifyOnValidationError、Validation.Errors、ValidationAttribute、IDataErrorInfo

~~~xaml
[ValueValidation]    // public  class ValueValidation : ValidationAttribute
[Required(ErrorMessage = "空，提示：必填《trans0067》")]
[StringLength(255, ErrorMessage = "[密码]内容最大允许255个字符！")]
[RegularExpression("^([0-4][0-9]|50)$|^(-[0-4][0-9]|-50)$", ErrorMessage = "输入框：-50到50，整数")]
~~~


~~~xaml
// Validation.ErrorTemplate
<Style TargetType="{x:Type TextBox}">
    <Setter Property="Validation.ErrorTemplate">
        <Setter.Value>
            <ControlTemplate>
                <DockPanel LastChildFill="True">
                    <!--<TextBlock DockPanel.Dock="Bottom" Foreground="Red"
           Text="{Binding ElementName=adorned,Path=AdornedElement.(Validation.Errors)[0].ErrorContent}"/>-->
                    <Border BorderBrush="Transparent" BorderThickness="1" ToolTip="{Binding ElementName=adorned,Path=AdornedElement.(Validation.Errors)[0].ErrorContent}">
                        <AdornedElementPlaceholder x:Name="adorned"/>
                    </Border>
                </DockPanel>
            </ControlTemplate>
        </Setter.Value>
    </Setter>
</Style>
// Notify
<Border  
        ToolTip="{Binding RelativeSource={x:Static RelativeSource.Self},
                 Path=(Validation.Errors)[0].ErrorContent}"
        Tag="{Binding ExpectedPowerModel.Value,Mode=TwoWay,
             UpdateSourceTrigger=PropertyChanged,
             ValidatesOnExceptions=True,
             ValidatesOnDataErrors=True,
             NotifyOnValidationError=True}"/>
~~~

~~~c#
// ValidationAttribute
class ValueValidation : ValidationAttribute
{
    public override bool IsValid(object value)
    {
        if (value == null || string.IsNullOrEmpty(value.ToString()))
        {
            ErrorMessage = "空，提示：必填《trans0067》";
            return false;
        }
        else
        {
            string pattern = @"^([0-4][0-9]|50)$|^(-[0-4][0-9]|-50)$";
            Match match = Regex.Match(value.ToString(), pattern);
            if (!match.Success)
            {
                ErrorMessage = "输入框：-50到50，整数";
                return false;
            }
            else
            {
                ErrorMessage = string.Empty;
                return true;
            }
        }
    }

    public override string FormatErrorMessage(string name)
    {
        return ErrorMessage;
    }
}
~~~



### DependencyObject

依赖属性是给自己用的，附加属性是给别人用的

#### DependencyProperty

Keys: DependencyProperty(依赖属性)、Register、PropertyMetadata、PropertyChangedCallbackHandler、CoerceValueCallbackHandler、ValidateValueCallbackHandler

~~~c#
// DependencyProperty: 封装数据，作用于动画、样式、绑定...
// ValidateValueCallback:	检查 属性值
// CoerceValueCallback: 	检查、强制赋值
// PropertyChangedCallback: 属性值变更回调
/* 输入数据，经过 ValidateValueCallback 进行数据验证，验证通过后，
在经过  CoerceValueCallback 进行数据转换，数据更改后，最后对应的
属性变更回调方法 PropertyChangedCallback */

public int MyAge
{
	get { return (int)GetValue(MyAgeProperty); }
	set { SetValue(MyAgeProperty, value); }
}

public static int DefaultAge = 18;

// 用于MyProperty的封装数据，它可以作用于动画，样式，绑定等等......
// Using a DependencyProperty as the backing store for MyProperty.  This enables animation, styling, binding, etc..
public static readonly DependencyProperty MyAgeProperty =
	DependencyProperty.Register("MyAge", typeof(int), typeof(Window), new PropertyMetadata(18, PropertyChangedCallbackHandler, CoerceValueCallbackHandler), ValidateValueCallbackHandler);

// 验证
private static bool ValidateValueCallbackHandler(object value)
{
	if (value is int iValue)
	{
		if (iValue > 100 || iValue < DefaultAge)
		{
			MessageBox.Show($"年龄 {iValue} 不在允许范围中！");
		}
	}
	return true;
}

// 强制转换
private static object CoerceValueCallbackHandler(DependencyObject d, object baseValue)
{
	if (baseValue is int iValue)
	{
		return iValue > 100 || iValue < DefaultAge ? DefaultAge : iValue;
	}
	else
	{
		return false;
	}
}

// 属性变更
private static void PropertyChangedCallbackHandler(DependencyObject d, DependencyPropertyChangedEventArgs e)
{
	if (d is Window win)
	{
		var txt = win?.FindName("TestTextBox") as TextBox;
		txt.BorderBrush = Brushes.GreenYellow;
	}
}
~~~



#### AttachedProperty

Keys: DependencyObject(依赖对象)、GetValue、SetValue

```c#
public class ContentTypeDpObj : DependencyObject
{
	/// <summary>
	/// 获取附加属性
	/// </summary>
	/// <param name="d"></param>
	/// <returns></returns>
	public static Type GetContentType(DependencyObject d)
	{
		return (Type)d.GetValue(ContentTypeProperty);
	}

	/// <summary>
	/// 设置附加属性
	/// </summary>
	/// <param name="d"></param>
	/// <param name="value"></param>
	public static void SetContentType(DependencyObject d, Type value)
	{
		d.SetValue(ContentTypeProperty, value);
	}
	// Using a DependencyProperty as the backing store for ContentType.  This enables animation, styling, binding, etc...
	public static readonly DependencyProperty ContentTypeProperty =
		DependencyProperty.Register("ContentType", typeof(Type), typeof(ContentTypeDpObj), new FrameworkPropertyMetadata(null, new PropertyChangedCallback(OnPropertyChanged)));

	private static void OnPropertyChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
	{
	}
}

public MainVM()
{
	navigateCmd = new RelayCommand<object>((para) =>
	{
		Type type = GetContentType(para);
		ConstructorInfo cti = type.GetConstructor(Type.EmptyTypes);
		this.MainContent = (FrameworkElement)cti.Invoke(null);

	}, (para) => true);

	NavigateCmd.Execute(typeof(HomePage));
}

private Type GetContentType(object para)
{
	Type type = null;
	if (para is Type)
	{
		type = para as Type;
	}
	else if (para is RadioButton rabtn)
	{
		// 获取 依赖对象 的 附加属性
		// var ss  = rabtn.GetValue(ContentTypeDp.ContentTypeProperty);
		type = ContentTypeDpObj.GetContentType(rabtn);
	}
	return type;
}
```



```xaml
<RadioButton
	common:ContentTypeDpObj.ContentType="{x:Type vm:HomePage}"
	Command="{Binding NavigateCmd}"
	CommandParameter="{Binding RelativeSource={RelativeSource Mode=Self}}"
	Content="Home"
	IsChecked="True"
	Style="{DynamicResource RadioBtnStyle.Navigation}" />
<RadioButton
	common:ContentTypeDpObj.ContentType="{x:Type vm:CenterPage}"
	Command="{Binding NavigateCmd}"
	CommandParameter="{Binding RelativeSource={RelativeSource Mode=Self}}"
	Content="Center"
	Style="{DynamicResource RadioBtnStyle.Navigation}" />
<RadioButton
	common:ContentTypeDpObj.ContentType="{x:Type vm:SettingPage}"
	Command="{Binding NavigateCmd}"
	CommandParameter="{Binding RelativeSource={RelativeSource Mode=Self}}"
	Content="Setting"
	Style="{DynamicResource RadioBtnStyle.Navigation}" />
```



```xaml
namespace GTS.MaxSign.Controls.Assets.Components
{
    public class ComboBoxHelper : DependencyObject
    {
        public static readonly DependencyProperty UnitProperty =
            DependencyProperty.RegisterAttached("Unit", typeof(string), typeof(ComboBoxHelper), new FrameworkPropertyMetadata("", new PropertyChangedCallback(Unit_OnPropertyChanged)));

        public static string GetUnit(DependencyObject d)
        {
            return d.GetValue(UnitProperty).ToString();
        }
        public static void SetUnit(DependencyObject d, string value)
        {
            d.SetValue(UnitProperty, value);
        }
        private static void Unit_OnPropertyChanged(DependencyObject d, DependencyPropertyChangedEventArgs e)
        {
            string unit = d.GetValue(UnitProperty).ToString();
        }
    }
}

<ComboBox  com:ComboBoxHelper.Unit="MHz"/>
<TextBlock Text="{DXBinding '$com:ComboBoxHelper.GetUnit(@p)'}" /> 

```





### Geometry

Keys:RectangleGeometry、EllipseGeometry、LineGeometry、PathGeometry

### Visual

Keys:DrawingVisual

### Path

Keys: F n、M x,y、Z、L x,y、A rx,ry,d f1(IsLargeArc) f2(Clockwise) x,y、C x1,y1 x2,y2 x,y、Q x1,y1 x,y、H x、V y、S x2,y2 x,y、DashStyle

```xaml
<Path Stroke="Black" StrokeThickness="1" Fill="#CCCCFF">
  <Path.Data>
    <PathGeometry Figures="M 10,100 C 10,300 300,-160 300,100" />
  </Path.Data>
</Path>

<Path Fill="Blue">
	<Path.Data>
		<EllipseGeometry
			x:Name="MyAnimatedEllipseGeometry"
			Center="10,100"
			RadiusX="15"
			RadiusY="15" />
	</Path.Data>
</Path>

<Path Fill="Blue">
	<Path.Data>
		<RectangleGeometry Rect="0,0,30,30" />
	</Path.Data>
</Path>

DashStyle:奇数位，宽度；偶数位，间距
<Pen Brush=”Black” Thickness=”10” DashStyle=”{x:Static DashStyles.DashDotDot}”/>

Data=”M 300,300 A 100,100 0 1 1 300,299 Z”

M 300,300: 表示起始坐标，字母 M 为 Move, 意思是将画笔移到 300,300 处
A:  表示 Arc 圆弧，
100,100:  表示圆弧宽高，圆是两值相同；
0 表示图形的旋转角度；
1 当图形设置了旋转角度，并且大于 180度时，才会生效，1 表示取大圆弧，0 表示取小圆弧；
1 表示画圆时笔画是是顺时针画，需要逆时针时设置为 0；
300,299 表示终止坐标
```



### Line

Keys：Stroke、StrokeDashArray、StrokeThickness、VisualBrush、StrokeStartLineCap/StrokeEndLineCap

~~~xaml
<Border>
	<!--Border.BorderBrush>
		<VisualBrush>
			<VisualBrush.Visual>
				<Rectangle
					Width="{Binding RelativeSource={RelativeSource AncestorType={x:Type Border}}, Path=ActualWidth}"
					Height="{Binding RelativeSource={RelativeSource AncestorType={x:Type Border}}, Path=ActualHeight}"
					Stroke="#D2D2D2"
					StrokeDashArray="4"
					StrokeThickness="0.8" />
			</VisualBrush.Visual>
		</VisualBrush>
	</Border.BorderBrush>-->
	<Line
		Stroke="#D2D2D2"
		StrokeDashArray="2"
		StrokeThickness="1"
		X1="0"
		X2="{Binding RelativeSource={RelativeSource AncestorType={x:Type Border}}, Path=ActualWidth}"
		Y1="1"
		Y2="1" />
</Border>
~~~

### Brush

Keys：SolidColorBrush、ColorConverter LinearGradientBrush

~~~C#
new SolidColorBrush(Color.FromArgb(0xFF, 0x36, 0xBF, 0x56));
new SolidColorBrush((Color)ColorConverter.ConvertFromString("#EEF7FF"));

LinearGradientBrush 
	StartPoint(x,y)	Default:(0,0)
	EndPoint (x,y)	Default:(1,1)
~~~



### Window

~~~xaml
WindowStartupLocation="CenterScreen" 
WindowStyle="None" 
AllowsTransparency="True"
ResizeMode="CanResizeWithGrip"	// 右下角 三角形 可缩放
~~~



### TextBox

Keys：InputMethod.IsInputMethodEnabled、PreviewTextInput、InputBindings、KeyBinding

~~~c#
// 只能输入数字
Step1.设置属性 InputMethod.IsInputMethodEnabled="False"		// 禁用输入法
Step2.注册事件 在控件中添加  PreviewTextInput="rlimitnumber"事件
public void limitnumber(object sender, TextCompositionEventArgs e)
{   
	 Regex re = new Regex("[^0-9]+");   
	 e.Handled = re.IsMatch(e.Text);
}

~~~

~~~xaml
// 按下 Enter 键 触发命令
<TextBox>
	<TextBox.InputBindings>
		<KeyBinding Key="Enter" Command="{Binding LoginCommand}"
		CommandParameter="{Binding ElementName=window}"/>
	</TextBox.InputBindings>
</TextBox>
~~~

### ContentControl

<img src="Images\content_control.png" style="zoom:50%;" />

```

```



### ButtonBase

Keys: ControlTemplate、ContentPresenter、ContentTemplate(DataTemplate)

```xaml
<ControlTemplate x:Key="TogButtonStyle" TargetType="{x:Type ButtonBase}">
	<ContentPresenter
		x:Name="contentPresenter"
		Margin="{TemplateBinding Padding}"
		HorizontalAlignment="{TemplateBinding HorizontalContentAlignment}"
		VerticalAlignment="{TemplateBinding VerticalContentAlignment}"
		dx:BlendHelper2.ThemeInfo="Core\Core\Themes\Office2019Colorful\StandardControls\Button.xaml;8;8"
		Content="{TemplateBinding Content}"
		ContentStringFormat="{TemplateBinding ContentStringFormat}"
		ContentTemplate="{TemplateBinding ContentTemplate}"
		Focusable="False"
		RecognizesAccessKey="True"
		SnapsToDevicePixels="{TemplateBinding SnapsToDevicePixels}" />
</ControlTemplate>
```





### Button

Keys：ControlTemplate、Triggers、IsMouseOver、IsPressed

~~~xaml
// IconFont-Button Style
<Style TargetType="Button" x:Key="WindowControlButtonStyle">
	<Setter Property="Width" Value="40"/>
	<Setter Property="Height" Value="30"/>
	<Setter Property="Foreground" Value="White"/>
	<Setter Property="Template">
		<Setter.Value>
			<ControlTemplate TargetType="Button">
				<Border Background="Transparent" Name="back">
					<TextBlock Text="{Binding Content,RelativeSource={RelativeSource AncestorType=Button,Mode=FindAncestor}}"
				   VerticalAlignment="Center" HorizontalAlignment="Center"
				   FontFamily="../Fonts/#iconfont" FontSize="16"/>
				</Border>
				<ControlTemplate.Triggers>
					<Trigger Property="IsMouseOver" Value="True">
						<Setter TargetName="back" Property="Background" Value="#22FFFFFF"/>
					</Trigger>
					<Trigger Property="IsPressed" Value="True">
						<Setter TargetName="back" Property="Background" Value="#44FFFFFF"/>
					</Trigger>
				</ControlTemplate.Triggers>
			</ControlTemplate>
		</Setter.Value>
	</Setter>
</Style>
// Blue Button Style
<ControlTemplate x:Key="LoginButtonTemplate" TargetType="Button">
	<Border Background="#007DFA" CornerRadius="5">
		<Grid>
			<Border
				Name="back"
				Background="#22FFFFFF"
				CornerRadius="4"
				Visibility="Hidden" />
			<ContentControl
				HorizontalAlignment="Center"
				VerticalAlignment="Center"
				Content="{TemplateBinding Content}"
				Foreground="{TemplateBinding Foreground}" />
		</Grid>
	</Border>
	<ControlTemplate.Triggers>
		<Trigger Property="IsMouseOver" Value="True">
			<Setter TargetName="back" Property="Visibility" Value="Visible" />
		</Trigger>
		<Trigger Property="IsEnabled" Value="False">
			<Setter TargetName="back" Property="Visibility" Value="Visible" />
			<Setter TargetName="back" Property="Background" Value="#EEE" />
			<Setter Property="Foreground" Value="#AAA" />
		</Trigger>
	</ControlTemplate.Triggers>
</ControlTemplate>

~~~



### RadioButton

Keys：ContentControl、TemplateBinding、Content

```xaml
<Style TargetType="RadioButton" x:Key="NavButtonStyle">
    <Setter Property="Foreground" Value="White"/>
    <Setter Property="Template">
        <Setter.Value>
            <ControlTemplate TargetType="RadioButton">
                <Border Background="Transparent" CornerRadius="8" Name="back">
                    <ContentControl Content="{TemplateBinding Content}" VerticalAlignment="Center" HorizontalAlignment="Center" Margin="20,4" FontSize="13"/>
                </Border>
                <ControlTemplate.Triggers>
                    <Trigger Property="IsChecked" Value="True">
                        <Setter TargetName="back" Property="Background" Value="#44FFFFFF"/>
                    </Trigger>
                </ControlTemplate.Triggers>
            </ControlTemplate>
        </Setter.Value>
    </Setter>
</Style>
```





### ComboBox

Keys: DisplayMemberPath

```xaml
<ComboBox
	x:Name="cmbFunc"
	Grid.Column="1"
	DisplayMemberPath="name"
	ItemsSource="{Binding Functions}"
	SelectionChanged="{DXEvent Handler='Function_SelectionChanged(@s,@args)'}" />
```





### DataGrid

Keys：DataGridColumnHeader 



### Border

Keys：Effect、DropShadowEffect、ShadowDepth、BlurRadius、ImageBrush

~~~xaml
// BlurRadius="5"：	模糊程度	
// Direction="0"：	相对于内容的角度
// Opacity="0.3"：	透明度
// ShadowDepth="0"：	与内容的距离，
// Color="Gray"：	颜色
<Border
	Width="90"
	Height="80"
	Margin="0,0,0,20"
	HorizontalAlignment="Center"
	VerticalAlignment="Center"
	CornerRadius="50">
	<Border.Effect>
		<DropShadowEffect
			BlurRadius="5"
			Direction="0"
			Opacity="0.3"
			ShadowDepth="0"
			Color="White" />
	</Border.Effect>
	<Border.Background>
		<ImageBrush ImageSource="../Assets/Images/Logo.png"></ImageBrush>
	</Border.Background>
</Border>
~~~



### ItemsControl

Keys：ItemContainerStyle、ItemTemplate、ItemsPanel、ItemsSource

```xaml
ItemsControl：ListBox、ListView，TreeView，TabControl
ItemContainerStyle 	(Item Style)
ItemTemplate		(Item DataTemplate)
ItemsPanelTemplate	(Items Panel)
```

Keys：ItemTemplateSelector (DataTemplateSelector)

```xaml
xmlns:ass="clr-namespace:WPFItemsControl.Assets"
<ItemsControl.ItemTemplateSelector>
	<ass:CourseDataTemplateSelector>
		<ass:CourseDataTemplateSelector.RealTemplate>
			<DataTemplate>
			...
			</DataTemplate>
		</ass:CourseDataTemplateSelector.RealTemplate>
		<ass:CourseDataTemplateSelector.SkeletonTemplate>
			<DataTemplate>
			...
			</DataTemplate>
		</ass:CourseDataTemplateSelector.SkeletonTemplate>
	</ass:CourseDataTemplateSelector>
</ItemsControl.ItemTemplateSelector>
```

```c#
public class CourseDataTemplateSelector : DataTemplateSelector
{
	public DataTemplate RealTemplate { get; set; }
	public DataTemplate SkeletonTemplate { get; set; }

	public override DataTemplate SelectTemplate(object item, DependencyObject container)
	{
		if ((item as CourseSeriesModel).IsShowSkeleton)
		{
			return SkeletonTemplate;
		}

		return RealTemplate;
		//return base.SelectTemplate(item, container);
	}
}
```





### ListView

Keys：ItemContainerStyle、ItemTemplate、ItemsPanel

```xaml

```



### TreeView

Keys：TreeView.Template(ControlTemplate)、TreeViewItem.Template(ControlTemplate)、ItemsPresenter

```xaml
<x:Array x:Key="templates" Type="{x:Type model:SingleTemplate}">
	<model:SingleTemplate
		Name="Template 1"
		IsAvailable="True"
		IsTemplateSelected="False"
		ParentBatID="1"
		State="0" />
	<model:SingleTemplate
		Name="Template 2"
		IsAvailable="True"
		IsTemplateSelected="False"
		ParentBatID="1"
		State="1" />
	<model:SingleTemplate
		Name="Template 3"
		IsAvailable="True"
		IsRenaming="True"
		IsTemplateSelected="False"
		ParentBatID="1"
		State="0" />
</x:Array>
<x:Array x:Key="Batches" Type="{x:Type model:BatchModel}">
	<model:BatchModel
		Name="BatchModel 1"
		ID="1"
		IsBatchSelected="False"
		IsSelected="True"
		Templates="{StaticResource templates}" />
	<model:BatchModel
		Name="BatchModel 2"
		ID="2"
		IsBatchSelected="False"
		Templates="{StaticResource templates}" />
	<model:BatchModel
		Name="BatchModel 3"
		ID="3"
		IsBatchSelected="True"
		IsExpanded="True"
		Templates="{StaticResource templates}" />
</x:Array>


<TreeView Name="tvTestQueue" ItemsSource="{StaticResource Batches}">
	<TreeView.Template>
		<ControlTemplate TargetType="{x:Type TreeView}">
			<Border BorderBrush="Red" BorderThickness="1">
				<ItemsPresenter />
			</Border>
		</ControlTemplate>
	</TreeView.Template>
	<TreeView.ItemContainerStyle>
		<Style TargetType="TreeViewItem">
			<Setter Property="IsExpanded" Value="True" />
			<!--<Setter Property="Template">
				<Setter.Value >
					<ControlTemplate TargetType="{x:Type TreeViewItem}">
					</ControlTemplate>
				</Setter.Value>
			</Setter>-->
		</Style>
	</TreeView.ItemContainerStyle>

	<TreeView.Resources>
		<HierarchicalDataTemplate DataType="{x:Type model:BatchModel}" ItemsSource="{Binding Templates}">
			<Grid>
				<Grid.RowDefinitions>
					<RowDefinition />
					<RowDefinition Height="1" />
				</Grid.RowDefinitions>
				<Border Name="groupBd" Margin="0">
					<StackPanel VerticalAlignment="Center" Orientation="Horizontal">
						<TextBlock
							x:Name="txtBlockTemplateSetsName"
							VerticalAlignment="Center"
							FontSize="12"
							FontWeight="Bold"
							Text="{Binding Name}"
							TextAlignment="Center"
							Visibility="{Binding IsRenaming, Converter={StaticResource BoolToInversedVisibilityConverter}}" />
						<TextBox
							x:Name="txtBoxTemplateSetsName"
							VerticalAlignment="Center"
							Focusable="True"
							FontSize="12"
							Tag="{Binding ID}"
							Text="{Binding Name}"
							TextAlignment="Left"
							ToolTip="{Binding Name}"
							Visibility="{Binding ElementName=txtBlockTemplateSetsName, Path=Visibility, Converter={StaticResource InversedVisibilityConverter}}" />

					</StackPanel>
				</Border>
				<Border
					Grid.Row="1"
					Background="#376BFA"
					Visibility="{Binding IsDragOver, Converter={StaticResource BoolToVisibilityConverter}}" />
			</Grid>
		</HierarchicalDataTemplate>

		<DataTemplate DataType="{x:Type model:SingleTemplate}">
			<Grid>
				<Grid.RowDefinitions>
					<RowDefinition />
					<RowDefinition Height="1" />
				</Grid.RowDefinitions>
				<Border
					Name="groupTemp"
					HorizontalAlignment="Stretch"
					Background="Transparent">
					<StackPanel
						VerticalAlignment="Center"
						IsEnabled="{Binding IsEnable}"
						Orientation="Horizontal">
						<TextBlock
							x:Name="txtBlockTemplateName"
							Margin="3,0,0,0"
							HorizontalAlignment="Left"
							VerticalAlignment="Center"
							Text="{Binding Name}"
							TextAlignment="Center"
							ToolTip="{Binding Name}"
							Visibility="{Binding IsRenaming, Converter={StaticResource BoolToInversedVisibilityConverter}}" />
						<TextBox
							x:Name="txtBoxTemplateName"
							HorizontalAlignment="Left"
							VerticalAlignment="Center"
							Focusable="True"
							Tag="{Binding TestId}"
							Text="{Binding Name}"
							TextAlignment="Center"
							ToolTip="{Binding Name}"
							Visibility="{Binding ElementName=txtBlockTemplateName, Path=Visibility, Converter={StaticResource InversedVisibilityConverter}}" />

						<TextBlock
							x:Name="txtBlockState"
							Margin="5,0,0,0"
							HorizontalAlignment="Left"
							VerticalAlignment="Center"
							Foreground="Red"
							Text="未完成"
							TextAlignment="Center"
							Visibility="{Binding State, Converter={StaticResource IntToVisibilityConverter}}" />
					</StackPanel>
				</Border>
				<Border
					Grid.Row="1"
					Background="#376BFA"
					Visibility="{Binding IsDragOver, Converter={StaticResource BoolToVisibilityConverter}}" />
			</Grid>

		</DataTemplate>
	</TreeView.Resources>
</TreeView>
```





### TabControl

Keys：ItemsControl、ItemsSource、ItemTemplate(DataTemplate)、ContentTemplate(DataTemplate)、ItemsPanel

~~~xaml
<TabControl
	MinHeight="150"
	Margin="0,7,0,0"
	ItemsSource="{Binding TabItems}"
	SelectedIndex="0">
	<TabControl.ItemTemplate>
		<DataTemplate DataType="{x:Type local:TabItem}">
			<TextBlock Text="{Binding Path=Header}" />
		</DataTemplate>
	</TabControl.ItemTemplate>
	<TabControl.ContentTemplate>
		<DataTemplate DataType="{x:Type local:TabItem}">
			<ItemsControl ItemsSource="{Binding AntennaPathlosses}">
				<ItemsControl.ItemTemplate>
					<DataTemplate DataType="{x:Type local:AntennaPathloss}">
						<StackPanel Margin="0,3,0,0" Orientation="Horizontal">
							<TextBlock
								Width="70"
								VerticalAlignment="Center"
								Text="{Binding Name, StringFormat='{}{0}：', Mode=TwoWay, UpdateSourceTrigger=PropertyChanged}"
								TextAlignment="Left" />
							<TextBlock
								MaxWidth="232"
								VerticalAlignment="Center"
								Text="{Binding Pathloss, Mode=TwoWay, UpdateSourceTrigger=PropertyChanged}"
								TextAlignment="Left"
								TextTrimming="CharacterEllipsis"
								ToolTip="{Binding Pathloss}" />
							<Button
								Width="60"
								Height="20"
								Margin="5,0"
								HorizontalAlignment="Right"
								Click="AntennaPathlossBtn_Click"
								Content="{StaticResource trans0157}"
								Style="{StaticResource GTSStyleButtonWhite}"
								Tag="{Binding}" />
						</StackPanel>
					</DataTemplate>
				</ItemsControl.ItemTemplate>

				<ItemsControl.ItemsPanel>
					<ItemsPanelTemplate>
						<VirtualizingStackPanel />
					</ItemsPanelTemplate>
				</ItemsControl.ItemsPanel>
			</ItemsControl>
		</DataTemplate>
	</TabControl.ContentTemplate>
</TabControl>
~~~

~~~csharp
public AntennaPathloss SingleAntennaPathloss { get; set; } = new AntennaPathloss();
public ObservableCollection<TabItem> TabItems { get; set; } = new ObservableCollection<TabItem>();
	
	
public class TabItem : NotifyPropertyChanged
{
	private string header;

	public string Header
	{
		get { return header; }
		set { header = value; OnPropertyChanged(); }
	}

	public ObservableCollection<AntennaPathloss> AntennaPathlosses { get; set; } = new ObservableCollection<AntennaPathloss>();
}

public class AntennaPathloss : NotifyPropertyChanged
{
	private string name;

	public string Name
	{
		get { return name; }
		set { name = value; OnPropertyChanged(); }
	}

	private string pathloss;

	public string Pathloss
	{
		get { return pathloss; }
		set { pathloss = value; OnPropertyChanged(); }
	}
}
~~~

### Expander

Keys：ExpandDirection、Hear、Content、IsExpanded

~~~xaml
<Expander ExpandDirection="Down" Width="96">
	<Expander.Header>
		<TextBlock Text="标题" FontWeight="Bold"/>
	</Expander.Header>
	<Expander.Content>
		<TextBlock TextWrapping="Wrap"  Text="这里是内容。"/>
	</Expander.Content>
</Expander> 
~~~

### Grid

Keys：

### GridSplitter

Keys：ResizeBehavior

```xaml
 <GridSplitter
                Grid.Column="1"
                Width="3"
                ResizeBehavior="PreviousAndNext" />
```



### UniformGrid

Keys：Columns、Resources、Style、TargetType

~~~xaml
<UniformGrid Columns="5" Grid.Row="1">
     <UniformGrid.Resources>
         <Style TargetType="TextBlock">
             <Style.Triggers>
                 <Trigger Property="IsMouseOver" Value="True">
                     <Setter Property="Foreground" Value="#007DFA"/>
                 </Trigger>
             </Style.Triggers>
         </Style>
     </UniformGrid.Resources>
     <TextBlock Text="&#xe71c;"/>
     <Border/>
     <TextBlock Text="&#xe601;"/>
     <Border/>
     <TextBlock Text="&#xe60c;"/>
</UniformGrid>
~~~





### Chart

#### ChartControl

Keys：DataSource、Titles、Legend、CrosshairOptions、ToolTipOptions、ToolTipController、Palette

~~~xaml
<dxc:ChartControl
	AnimationMode="OnLoad"
	CrosshairEnabled="True"
	DataSource="{Binding XY2DModel.PointsData}"
	ToolTipEnabled="False">
	<dxc:ChartControl.Legend>
		<dxc:Legend
			HorizontalPosition="Left"
			MarkerMode="CheckBoxAndMarker"
			Orientation="Vertical"
			ReverseItems="False"
			VerticalPosition="Center"
			Visibility="Collapsed" />
	</dxc:ChartControl.Legend>
	<dxc:ChartControl.Titles>
		<dxc:Title
			HorizontalAlignment="Center"
			Content="ChartControl Title"
			Dock="Top"
			Visibility="Collapsed" />
	</dxc:ChartControl.Titles>
	<dxc:ChartControl.CrosshairOptions>
		<dxc:CrosshairOptions
			ContentShowMode="Label"
			CrosshairLabelMode="ShowCommonForAllSeries"
			GroupHeaderPattern="{}{A}°"
			LinesMode="Auto"
			ShowArgumentLabels="True"
			ShowGroupHeaders="True" />
	</dxc:ChartControl.CrosshairOptions>
	<dxc:ChartControl.ToolTipOptions>
		<dxc:ToolTipOptions
			ShowForPoints="True"
			ShowForSeries="False"
			ShowHint="False">
			<dxc:ToolTipOptions.ToolTipPosition>
				<dxc:ToolTipMousePosition Location="TopLeft" />
			</dxc:ToolTipOptions.ToolTipPosition>
		</dxc:ToolTipOptions>
	</dxc:ChartControl.ToolTipOptions>
	<dxc:ChartControl.ToolTipController>
		<dxc:ChartToolTipController
			AutoPopDelay="0"
			CloseOnClick="False"
			ContentMargin="1"
			InitialDelay="0:0:0.1"
			OpenMode="OnHover"
			ShowBeak="False"
			ShowShadow="False"
			ToolTipOpening="ChartToolTipController_ToolTipOpening" />
	</dxc:ChartControl.ToolTipController>
	<dxc:ChartControl.Palette>
		<dxc:CustomPalette>
			<dxc:CustomPalette.Colors>
				<Color>#c32136</Color>
				<Color>#e4c6d0</Color>
				<Color>#cca4e3</Color>
				<Color>#789262</Color>
				<Color>#493131</Color>
			</dxc:CustomPalette.Colors>
		</dxc:CustomPalette>
	</dxc:ChartControl.Palette>
</dxc:ChartControl>
~~~



#### XYDiagram2D

Keys：EnableAxisXNavigation、EnableAxisYNavigation、SeriesDataMember、SeriesTemplate、AxisX(Title，CrosshairAxisLabelOptions，ScaleOptions，WholeRange)、AxisY、DefaultPane、NavigationOptions、

~~~xaml
<dxc:XYDiagram2D
	Margin="-10,0,-2,0"
	EnableAxisXNavigation="{Binding XY2DModel.NavigationModel.EnableAxisX}"
	EnableAxisYNavigation="{Binding XY2DModel.NavigationModel.EnableAxisY}"
	SeriesDataMember="ModeLegend">
	<dxc:XYDiagram2D.AxisX>
		<dxc:AxisX2D
			Alignment="Near"
			GridLinesMinorVisible="True"
			GridLinesVisible="True"
			Interlaced="False"
			MinorCount="10"
			TickmarksMinorVisible="True">
			<dxc:AxisX2D.Title>
				<dxc:AxisTitle
					Content="{DynamicResource trans0032}"/>
			</dxc:AxisX2D.Title>
			<dxc:AxisX2D.CrosshairAxisLabelOptions>
				<dxc:CrosshairAxisLabelOptions Pattern="{}{A:0}°" />
			</dxc:AxisX2D.CrosshairAxisLabelOptions>
			<!--<dxc:AxisX2D.Label>
				<dxc:AxisLabel TextPattern="{}{A}°"  />
			</dxc:AxisX2D.Label>-->
			<dxc:AxisX2D.NumericScaleOptions>
				<!--<dxc:AutomaticNumericScaleOptions AggregateFunction="Maximum" />-->
				<dxc:ManualNumericScaleOptions
					AggregateFunction="None"
					AutoGrid="False"
					GridSpacing="20" />
				<!--<dxc:ContinuousNumericScaleOptions />-->
				<!--<dxc:IntervalNumericScaleOptions AutoGrid="True"  ></dxc:IntervalNumericScaleOptions>-->
			</dxc:AxisX2D.NumericScaleOptions>

			<dxc:AxisX2D.WholeRange>
				<dxc:Range
					dxc:AxisY2D.AlwaysShowZeroLevel="True"
					MaxValue="{Binding XY2DModel.AxisXModel.RangeMax}"
					MinValue="{Binding XY2DModel.AxisXModel.RangeMin}"
					SideMarginsValue="0" />
			</dxc:AxisX2D.WholeRange>
		</dxc:AxisX2D>
	</dxc:XYDiagram2D.AxisX>
	<dxc:XYDiagram2D.AxisY>
		<dxc:AxisY2D
			GridLinesMinorVisible="True"
			GridLinesVisible="True"
			Interlaced="False"
			TickmarksMinorVisible="True">
			<dxc:AxisY2D.Title>
				<dxc:AxisTitle
					Padding="0"
					Content="{Binding XY2DModel.AxisYModel.Title}"/>
			</dxc:AxisY2D.Title>
			<dxc:AxisY2D.Label>
				<dxc:AxisLabel Padding="0" />
			</dxc:AxisY2D.Label>
			<dxc:AxisY2D.WholeRange>
				<dxc:Range dxc:AxisY2D.AlwaysShowZeroLevel="False" />
			</dxc:AxisY2D.WholeRange>
		</dxc:AxisY2D>
	</dxc:XYDiagram2D.AxisY>
	<dxc:XYDiagram2D.DefaultPane>
		<dxc:Pane>
			<dxc:Pane.AxisXScrollBarOptions>
				<dxc:ScrollBarOptions BarThickness="10" Visible="True" />
			</dxc:Pane.AxisXScrollBarOptions>
			<dxc:Pane.AxisYScrollBarOptions>
				<dxc:ScrollBarOptions
					Alignment="Near"
					BarThickness="10"
					Visible="True" />
			</dxc:Pane.AxisYScrollBarOptions>
		</dxc:Pane>
	</dxc:XYDiagram2D.DefaultPane>
	<dxc:XYDiagram2D.NavigationOptions>
		<dxc:NavigationOptions
			AxisXMaxZoomPercent="2500"
			AxisYMaxZoomPercent="2500"
			UseKeyboard="True"
			UseMouse="True"
			UseScrollBars="True" />
	</dxc:XYDiagram2D.NavigationOptions>
</dxc:XYDiagram2D>
~~~

Keys：PaneItemsSource、SeriesItemsSource、SecondaryAxisYItemsSource

~~~xaml
<dxc:XYDiagram2D
PaneItemsSource="{Binding Panes}"
SeriesItemsSource="{Binding SensorDataSeries}"
SecondaryAxisYItemsSource="{Binding Panes}"
EnableAxisXNavigation="True"
BeforeZoom="{DXEvent '@c.LimitZoom(@args)'}"/>
~~~



#### LineSeries2D

Keys：AllowResample、AnimationAutoStartMode、ArgumentDataMember、CrosshairContentShowMode、CrosshairLabelPattern、LabelsVisibility、MarkerSize、MarkerVisible、ShowInLegend、ToolTipPointPattern、ValueDataMember；LegendMarkerTemplate、MarkerModel(PointTemplate，)、LineStyle、SeriesAnimation、PointAnimation、Label、ToolTipPointTemplate

~~~xaml
<dxc:LineSeries2D
	x:Name="series"
	AllowResample="False"
	AnimationAutoStartMode="SetFinalState"
	ArgumentDataMember="Theta"
	CrosshairContentShowMode="Label"
	CrosshairLabelPattern="{}{S} : {V:0.00} dB"
	LabelsVisibility="False"
	MarkerSize="7"
	MarkerVisible="False"
	ShowInLegend="True"
	ToolTipPointPattern="{}{A}°,{V:0.00}"
	ValueDataMember="Gain">
	<dxc:LineSeries2D.LegendMarkerTemplate>
		<DataTemplate>
			<StackPanel Orientation="Horizontal">
				<Grid Width="12" Height="12">
					<Ellipse
						x:Name="ellipse"
						Stretch="Uniform"
						Stroke="{Binding Path=MarkerLineBrush}"
						StrokeDashArray="{Binding Path=MarkerLineStyle.DashStyle.Dashes}"
						StrokeThickness="{Binding Path=MarkerLineStyle.Thickness}" />
				</Grid>
				<TextBlock
					Width="55"
					Margin="4,0,0,0"
					VerticalAlignment="Center"
					Text="{Binding Path=Text}" />
			</StackPanel>
		</DataTemplate>
	</dxc:LineSeries2D.LegendMarkerTemplate>
	<dxc:LineSeries2D.MarkerModel>
		<dxc:SimpleMarker2DModel />
	</dxc:LineSeries2D.MarkerModel>
	<dxc:LineSeries2D.LineStyle>
		<dxc:LineStyle LineJoin="Round" Thickness="1" >
			<DashStyle Dashes="" Offset="0" />
		</dxc:LineStyle.DashStyle>-->
		</dxc:LineStyle>
	</dxc:LineSeries2D.LineStyle>
	<dxc:LineSeries2D.Label>
		<dxc:SeriesLabel>
			<dxc:SeriesLabel.
		</dxc:SeriesLabel>
	</dxc:LineSeries2D.Label>
	<dxc:LineSeries2D.SeriesAnimation>
		<dxc:Line2DBlowUpAnimation />
	</dxc:LineSeries2D.SeriesAnimation>
	<dxc:LineSeries2D.PointAnimation>
		<dxc:Marker2DFadeInAnimation />
	</dxc:LineSeries2D.PointAnimation>
	<dxc:LineSeries2D.Label>
		<dxc:SeriesLabel
			dxc:MarkerSeries2D.Angle="45"
			ConnectorVisible="False"
			Indent="5"
			ResolveOverlappingMode="Default" />
	</dxc:LineSeries2D.Label>
	<dxc:LineSeries2D.ToolTipPointTemplate>
		<DataTemplate>
			<Grid>
				<Label Content="{Binding ToolTipText}" FontSize="12" />
			</Grid>
		</DataTemplate>
	</dxc:LineSeries2D.ToolTipPointTemplate>
</dxc:LineSeries2D>
~~~



### Experience

> 1. 运行时 XAML 中的异常 不会被断点捕获到；
>
> 2. Binding时，模型属性一定 要添加 属性访问器 { get; set; }；
>
> 3. 添加现有文件，将文件属性中的生成操作设置为 Resource， 否则定位不到文件位置；
>
> 4. 只能针对 DependencyProperty 进行 Binding，不能针对 Property Binding；
>
> 5. Window 下设置 Border.Effect，不仅会严重损耗性能，而且在DropShadowEffect的Border内部添加展示的元素文本会模糊；
>
> 	~~~xaml
> 	<Border>
> 		<Border.Effect>
> 		 <DropShadowEffect
> 			BlurRadius="3"
> 			ShadowDepth="0"
> 			Color="LightGray" />
> 		</Border.Effect>
> 	</Border>
> 	~~~
>
> 6. Style 无法识别本地元素，ElementName 和 绑定的源属性; 
>
> 7. Validation.ErrorTemplate 默认红框不显示，原因：Window类默认的Style包含AdornerDecorator元素， 而UserControl没有。 主要是因为UserControl经常应用在Window里或者其他上下文已经有了AdornerLayer，
>
> 	~~~xaml
> 	解决办法： 在UserControl的逻辑树的根下添加AdornerDecorator， 如：
> 	<UserControl>
> 	     <AdornerDecorator>
> 	          <Grid Background="Yellow">
> 	               ...
> 	          </Grid>
> 	     </AdornerDecorator>
> 	</UserControl>
> 	~~~
>
> 8. 若干个 Control 同时叠加在同一个 Grid 上，可设置 VerticalAlignment 、HorizontalAlignment 以及 Margin 属性，调整 Control 间的相对位置，从而无须创建多余的行和列；
>
> 9. Style 中的  DataTrigger 允许 Binding 的源属性：依赖属性、DataContext 的模型属性。
>
> 	```xaml
> 	<Button>
> 		<Button.Style>
> 			<Style TargetType="Button">
> 				<Style.Triggers>
> 					<DataTrigger Binding="{Binding DataContext.ShowProgress, RelativeSource={RelativeSource Mode=FindAncestor, AncestorType=Window}}" Value="Visible">
> 						<Setter Property="IsEnabled" Value="False" />
> 					</DataTrigger>
> 				</Style.Triggers>
> 			</Style>
> 		</Button.Style>
> 	</Button>
> 	```
>
> 10. Stack 中的 ScrollViewer 无效，而 ScrollViewer -> ItemsControl 有效(超出会出现 Scroll)
>
> 11. XAML 引用 CS 枚举、静态、常量字符串
>
> 	```xaml
> 	xmlns:model="clr-namespace:Auto_OTA.Model"
>
> 	<DataTrigger Binding="{Binding State}" Value="{x:Static model:TestTaskState.Prepare }">
> 		<Setter TargetName="PART_TxtState" Property="Text" Value="&#xe61d;"/>
> 	</DataTrigger>
> 	```
>
> 	```c#
> 	/// <summary>
> 	/// 测试任务状态
> 	/// </summary>
> 	public enum TestTaskState
> 	{
> 		/// <summary>
> 		/// 未开始/已取消
> 		/// </summary>
> 		Prepare,
> 		/// <summary>
> 		/// 测试完成
> 		/// </summary>
> 		Done,
> 	}
> 	```
>
> 12. 找不到究竟是谁的 SrcollView Bar？运行起来 --> 查看可视化树 --> 查看源
>
> 13. 当父容器 ScrollViewer.HorizontalScrollBarVisibility="Disabled" ，子控件 DataGrid 自动铺满
>
> 14. StackPanel 无滚动条？解：在 StackPanel 外加 ScrollViewer，并设置 ScrollViewer MaxHeight
>
> 15. ComboBox 的   DisplayMemberPath="name" 的属性 需要 get ; set ;,  public string name { get; set; }
>
> 16. DxTheme 会影响 原始控件的样式 和 行为
>
> 17. 使用了 DevExpress UI层中的异常可能不会导致主程序异常退出
>
> 18. WPF Popup 中 IME 不跟随 TextBox
>
> 	```xaml
> 	 <Popup Opened="PART_Popup_Opened"/>
> 	```
>
> 	```c#
> 	[DllImport("User32.dll")]
> 	public static extern IntPtr SetFocus(IntPtr hWnd);
> 							
> 	private IntPtr GetHwnd(Popup popup)
> 	{
> 	    HwndSource source = (HwndSource)PresentationSource.FromVisual(popup.Child);
> 	    return source.Handle;
> 	}
> 							
> 	private void PART_Popup_Opened(object sender, System.EventArgs e)
> 	{
> 	    Popup popup = sender as Popup;
> 	    IntPtr handle = GetHwnd(popup);
> 	    SetFocus(handle);
> 	}
> 	```
>
> 	19.整体布局用 Grid，局部模块用 HorizontalAlignment、VerticalAlignment + Margin 调整，局部细节可选 Grid、xxxPanel 等

