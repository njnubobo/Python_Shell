## Python 开发一个自己的shell

* shell_loop()函数

  启动Shell时，会展示提示符并等待，在接受命令后执行，执行完继续等待命令。status标志来表示循环是否继续。在循环开始时，shell立即显示提示符，等待输入，输入完后对命令进行切分和执行。

* tokenize()函数

  对命令进行切分，在这里可以直接使用Python的一个库shlex。
  
  > shlecx.split() 
  
  可以帮我们分词，也可以用正则表达式，稍微烦一些。然后将这些token传给执行进程。
  
* execute()函数

  shell的核心部分，
  
  > os.execvp()
  
  是系统调用exec的一个变种。第一个参数是程序名。v表示第二个参数是程序参数列表（可变的参数个数）。p表示PATH环境将用于搜集给你的程序名。
  这里要用到子进程，因为exec会将当前调用进程的内存替换为即将执行的进程。如果不使用子进程，那么在一条指令执行完毕之后shell会退出不会继续等待下一条指令
  因为此时的shell进程已经被替换。
  
* fork使用
  
  execute()创建子进程之后，如果运行的进程是子进程，则pid为0，否则pid为子进程的id。父进程等待子进程结束之后会返回shell循环的状态。
  
  **to be continued...**
  
