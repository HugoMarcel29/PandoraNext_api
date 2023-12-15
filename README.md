# PandoraNext_api
<h1>使用ChatGPT PandoraNext的API实例</h1>
<h3>使用前请自架设服务器，并在配置文件中设置API服务前缀。代码中需修改自架设的PandoraNext的服务器地址。


<h1>一、PandoraNext_completion.py</h1>
<h3>采用completion模式，只能单次对话+回复

可使用share tocken或pool tocken（推荐）登录



<h1>二、PandoraNext_Conversation.py</h1>
<h3>采用Conversation模式，跟网页一样可以上下文多次对话。

使用access tocken或session tocken登录

如不指定会话编号则新建一个会话，同时反馈会话编号和父信息编号；

下一次请求的时候则可指定会话编号和父信息编号，这样就可以实现上下文结合多次对话了。


