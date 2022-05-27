Node.js is a virtual machine that uses JavaScript as its scripting language and runs Chrome’s V8 JavaScript engine.
Npm or Yarn is the package manager for NodeJs.

Node Advantages
  1. Chrome V8 - Runs on C++
  2. Javascript on Both Frontend and Backend

The main advantage of using promise is you get an object to decide the action that needs to be taken after the async task completes. 
This gives more manageable code and avoids callback hell.

Types of function in Node.js
  1. Asyncronous 
  2. Syncronous 

module.export()

Exit codes give us an idea of how a process got terminated/the reason behind termination. 

Stubs are used in writing tests which are an important part of development. It replaces the whole function which is getting tested.  

  Node.js applications run on a single processor, which means that by default they don’t take advantage of a multiple-core system. 
  Cluster mode is used to start up multiple node.js processes thereby having multiple instances of the event loop. 
  When we start using cluster in a nodejs app behind the scene multiple node.js processes are created but there is also a parent process called the 
  cluster manager which is responsible for monitoring the health of the individual instances of our application.

  The main loop is single-threaded and all async calls are managed by libuv library.
