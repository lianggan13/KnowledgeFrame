## WPF



### MVVM Foundation

![](Images\mvvm_foundation_frame.PNG)

> + Messenger：View和ViewModel 以及 ViewModel和ViewModel 之间的消息通知和接收
> + ObservableObject：等价于ViewModelBase，被ViewModel继承，调用完成后立即释放，防止内存泄漏
> + PropertyObserver：封装INotifyPropertyChanged.PropertyChanged，通过其对某个对象的属性变更注册回调函数，当属性变更时触发回调函数
> + RelayCommand：封装Command，包括execution执行逻辑等



### Binding

Bind Mode

 One Way:            UI <---- Model (UI Get)

 One Way to Source:   UI ----> Model (UI Set)

 Default(Two Way):    UI <---> Model (UI Get & Set)

### Trigger

- Keys：Property Trigger、Binding DataTrigger、ControlTemplate.Triggers、MultiDataTrigger、EventTrigger(RouteEvent、Actions、Storyboard)、EventSetter

	~~~xaml
	// Property Trigger
	<Style.Triggers>
		<Trigger Property="IsSelected" Value="True">
			<Setter Property="Background" Value="White" />
		</Trigger>
		<Trigger Property="IsMouseOver" Value="True">
			<Setter Property="Background" Value="White"/>
		</Trigger>
	</Style.Triggers>
	// Binding DataTrigger
	<Style.Triggers>
		<DataTrigger Binding="{Binding IsEnabled}" Value="true">
			<Setter Property="Cursor" Value="Hand"/>
		</DataTrigger>
		<DataTrigger Binding="{Binding IsEnabled}" Value="false">
			<Setter Property="Cursor" Value="Arrow"/>
		</DataTrigger>
	</Style.Triggers>
	// ControlTemplate.Triggers
	<ControlTemplate TargetType="{x:Type ListViewItem}">
		<Border Name="BD_Collector" Background="White" Width="auto" Height="28" Margin="2">
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
	// MultiDataTrigger 
	<MultiDataTrigger>
		<MultiDataTrigger.Conditions>
			<Condition Binding="{Binding IsEditable, RelativeSource={RelativeSource AncestorType={x:Type ComboBox}}}" Value="true"/>
			<Condition Binding="{Binding IsMouseOver, RelativeSource={RelativeSource Self}}" Value="false"/>
			<Condition Binding="{Binding IsPressed, RelativeSource={RelativeSource Self}}" Value="false"/>
			<Condition Binding="{Binding IsEnabled, RelativeSource={RelativeSource Self}}" Value="true"/>
		</MultiDataTrigger.Conditions>
		<Setter Property="BorderBrush" TargetName="templateRoot" Value="#FF565656"/>
	</MultiDataTrigger>
	// EventTrigger
	<ControlTemplate x:Key="customMarkerPointTemplate">
		<Grid x:Name="model" Background="Transparent" RenderTransformOrigin="0.5,0.5">
			<Grid.RenderTransform>
				<ScaleTransform />
			</Grid.RenderTransform>
			<Ellipse
				Stroke="{Binding Path=PointColor, ConverterParameter=Gray, Converter={StaticResource brushOverlayConverter}}"
				StrokeThickness="2" />
			<Ellipse
				Stroke="{Binding Path=PointColor, ConverterParameter=Gray, Converter={StaticResource brushOverlayConverter}}"
				StrokeThickness="2"
				Margin="4" />
			<Ellipse
				Margin="8"
				Opacity="{Binding Opacity}"
				Fill="{Binding Path=PointColor, ConverterParameter=Gray, Converter={StaticResource brushOverlayConverter}}" />
			<Grid.Triggers>
				<EventTrigger
					RoutedEvent="MouseEnter">
					<BeginStoryboard>
						<Storyboard
							TargetName="model">
							<DoubleAnimation
								Duration="0:0:0.25"
								To="1.5"
								Storyboard.TargetProperty="(UIElement.RenderTransform).(ScaleTransform.ScaleX)">
								<DoubleAnimation.EasingFunction>
									<BackEase
										Amplitude="2"
										EasingMode="EaseOut" />
								</DoubleAnimation.EasingFunction>
							</DoubleAnimation>
							<DoubleAnimation
								Duration="0:0:0.25"
								To="1.5"
								Storyboard.TargetProperty="(UIElement.RenderTransform).(ScaleTransform.ScaleY)">
								<DoubleAnimation.EasingFunction>
									<BackEase
										Amplitude="2"
										EasingMode="EaseOut" />
								</DoubleAnimation.EasingFunction>
							</DoubleAnimation>
						</Storyboard>
					</BeginStoryboard>
				</EventTrigger>
				<EventTrigger
					RoutedEvent="MouseLeave">
					<BeginStoryboard>
						<Storyboard
							TargetName="model">
							<DoubleAnimation
								Duration="0:0:0.5"
								To="1"
								Storyboard.TargetProperty="(UIElement.RenderTransform).(ScaleTransform.ScaleX)">
								<DoubleAnimation.EasingFunction>
									<CircleEase
										EasingMode="EaseOut" />
								</DoubleAnimation.EasingFunction>
							</DoubleAnimation>
							<DoubleAnimation
								Duration="0:0:0.5"
								To="1"
								Storyboard.TargetProperty="(UIElement.RenderTransform).(ScaleTransform.ScaleY)">
								<DoubleAnimation.EasingFunction>
									<CircleEase
										EasingMode="EaseOut" />
								</DoubleAnimation.EasingFunction>
							</DoubleAnimation>
						</Storyboard>
					</BeginStoryboard>
				</EventTrigger>
			</Grid.Triggers>
		</Grid>
	</ControlTemplate>
	// EventSetter
	<EventSetter Event="LostFocus" Handler="ListBoxItem_LostFocus"/>
	~~~

### Command

 - Keys：Command、CommandParameter、EventTrigger、CallMethodAction、InvokeCommandAction

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

	

	

	

	

### Template

#### ControlTemplate	

- Keys：ListViewItem、ControlTemplate.Triggers、TargetName

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

### DependencyProperty

Keys：DependencyProperty、Register

~~~c#
public class ImageButton : RadioButton
{
    public static readonly DependencyProperty NormalImgSourceProperty = DependencyProperty.Register(
        "NormalImgSource", typeof(ImageSource), typeof(ImageButton), new PropertyMetadata(null));

    public ImageSource NormalImgSource
    {
        get { return (ImageSource)GetValue(NormalImgSourceProperty); }
        set { SetValue(NormalImgSourceProperty, value); }
    }

    public static readonly DependencyProperty HoverImgSourceProperty = DependencyProperty.Register(
        "HoverImgSource", typeof(ImageSource), typeof(ImageButton), new PropertyMetadata(null));

    public ImageSource HoverImgSource
    {
        get { return (ImageSource)GetValue(HoverImgSourceProperty); }
        set { SetValue(HoverImgSourceProperty, value); }
    }

    public static readonly DependencyProperty CheckedImgSourceProperty = DependencyProperty.Register(
        "CheckedImgSource", typeof(ImageSource), typeof(ImageButton), new PropertyMetadata(null));
    public ImageSource CheckedImgSource
    {
        get { return (ImageSource)GetValue(CheckedImgSourceProperty); }
        set { SetValue(CheckedImgSourceProperty, value); }
    }

    static ImageButton()
    {
        DefaultStyleKeyProperty.OverrideMetadata(typeof(ImageButton), new FrameworkPropertyMetadata(typeof(ImageButton)));

    }
}
~~~



### AttachedProperty List

> + Validation
> + FocusManager
> + ToolTipService

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

### Color

Keys：SolidColorBrush、ColorConverter

~~~C#
new SolidColorBrush(Color.FromArgb(0xFF, 0x36, 0xBF, 0x56));
new SolidColorBrush((Color)ColorConverter.ConvertFromString("#EEF7FF"));
~~~



### Window

~~~xaml
WindowStartupLocation="CenterScreen" 
WindowStyle="None" 
AllowsTransparency="True"
ResizeMode="CanResizeWithGrip"	// 右下角 三角形 可缩放
~~~



### TextBox

Keys：InputMethod.IsInputMethodEnabled、PreviewTextInput

~~~c#
// 只能输入数字
Step1.设置属性 InputMethod.IsInputMethodEnabled="False"		// 禁用输入法
Step2.注册事件 在控件中添加  PreviewTextInput="rlimitnumber"事件
public void limitnumber(object sender, TextCompositionEventArgs e)
{   
	 Regex re = new Regex("[^0-9]+");   
	 e.Handled = re.IsMatch(e.Text);
}
// 按下 Enter 键 触发命令
<TextBox>
	<TextBox.InputBindings>
		<KeyBinding Key="Enter" Command="{Binding LoginCommand}"
		CommandParameter="{Binding ElementName=window}"/>
	</TextBox.InputBindings>
</TextBox>
~~~

### ComboBox



### DataGrid

Keys：DataGridColumnHeader



### Border

Keys：Effect、DropShadowEffect、ShadowDepth、BlurRadius

~~~xaml
<Border Width="80" Height="80"  VerticalAlignment="Center" HorizontalAlignment="Center"
        CornerRadius="50"  Margin="0,0,0,20">
    <Border.Effect>
        <DropShadowEffect Color="White" ShadowDepth="0" BlurRadius="5" Opacity="0.3" Direction="0"/>
    </Border.Effect>
    <Border  Width="90" Height="80" HorizontalAlignment="Center">
        <Border.Background>
            <ImageBrush ImageSource="../Assets/Images/Logo.png"/>
        </Border.Background>
    </Border>
    <!--<Border.Background>
        	<ImageBrush ImageSource="../Assets/Images/Logo.png"/>
    </Border.Background>-->
</Border>
~~~





### ListView

Keys：ItemContainerStyle、



### TreeView

Keys：ItemContainerStyle、Header



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

### UniformGrid

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
> 6. Style 无法识别本地元素，ElementName; 
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
> 	

