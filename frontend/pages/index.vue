<template>

  <div>
  <nav class="bg-gray-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <div class="flex-shrink-0">
            <img class="h-8 w-8" src="../static/dashboard.svg" alt="Dashboard logo" />
          </div>
          <div class="hidden md:block">
            <div class="ml-10 flex items-baseline">
              <a href="#" class="px-3 py-2 rounded-md text-sm font-medium text-white bg-gray-900 focus:outline-none focus:text-white focus:bg-gray-700">Dashboard
              </a>
            </div>
          </div>
        </div>
        <div class="hidden md:block">
          <div class="ml-4 flex items-center md:ml-6">
            <div class="ml-3 relative">
              <div>
                <button  @click="showNotification = !showNotification" class="relative z-10 max-w-xs flex items-center text-sm rounded-full text-white focus:outline-none " id="user-notification" aria-label="User menu" aria-haspopup="true">
                  <svg class="h-6 w-6" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
                </svg>
                </button>
                <button v-if="showNotification" @click="showNotification = false" tabindex = "-1" class="fixed inset-0 w-full h-full bg-black opacity-50 cursor-default"></button>
              </div>
              <div v-if="showNotification" class="origin-top-right absolute right-0 mt-2 w-screen max-w-sm sm:max-w-md md:max-w-lg lg:max-w-xl rounded-md shadow-lg">
                <div class="py-1 rounded-md bg-white shadow-xs" role="menu" aria-orientation="vertical" aria-labelledby="user-notification">
                  <div v-if="Math.abs(notificationlist.length) > 0" v-for="notification in notificationlist" :key="notification.index" class="bg-white even:bg-gray-200">
                    <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
                      <div class="m-2">{{ notification.text }}</div>  
                    </div>
                  </div>
                  <div v-else class="bg-white even:bg-gray-200">
                    <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
                      <div class="m-2">Notifications right now! ajao</div>  
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Profile dropdown -->
            <div class="ml-3 relative">
              <div>
                <button  @click="isOpen = !isOpen" class="relative z-10 max-w-xs flex items-center text-sm rounded-full text-white focus:outline-none focus:shadow-solid" id="user-menu" aria-label="User menu" aria-haspopup="true">
                  <img class="h-8 w-8 rounded-full bg-white" src="../static/person.png" alt="" />
                </button>
                <button v-if="isOpen" @click="isOpen = false" tabindex = "-1" class="fixed inset-0 w-full h-full bg-black opacity-50 cursor-default"></button>
              </div>
              <div v-if="isOpen" class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg">
                <div class="py-1 rounded-md bg-white shadow-xs" role="menu" aria-orientation="vertical" aria-labelledby="user-menu">
                  <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Some Lorem Setting
                  </a>
                  <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Sign out
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="-mr-2 flex md:hidden">
          <!-- Mobile menu button -->
          <button class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:bg-gray-700 focus:text-white">
            <!-- Menu open: "hidden", Menu closed: "block" -->
            <svg class="block h-6 w-6" stroke="currentColor" fill="none" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
            <!-- Menu open: "block", Menu closed: "hidden" -->
            <svg class="hidden h-6 w-6" stroke="currentColor" fill="none" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!--
      Mobile menu, toggle classes based on menu state.

      Open: "block", closed: "hidden"
    -->
    <div class="hidden md:hidden">
      <div class="px-2 pt-2 pb-3 sm:px-3">
        <a href="#" class="block px-3 py-2 rounded-md text-base font-medium text-white bg-gray-900 focus:outline-none focus:text-white focus:bg-gray-700">Dashboard
        </a>
      </div>
    </div>
  </nav>

  <header class="bg-white shadow">
    <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
      <h6 class="text-2xl font-bold leading-tight text-gray-900">
        Welcome {{name}},
      </h6>
      <!-- <p>{{ countRequest}}</p> <button v-on:click="getCount()">Get count</button> -->
    </div>
  </header>
  <main>
    <div class="max-w-7xl mx-auto py-3 sm:px-6 lg:px-8">
      <div class="px-2 py-3 sm:px-0">
        <div class="border-4 border-solid border-gray-200 rounded-lg">
          <div class="flex flex-row border-2 border-gray-100 p-2 m-auto bg-white shadow-lg">
            <button v-on:click="getCount()" class="bg-transparent hover:bg-green-500 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-500 hover:border-transparent rounded float-right">
                Request Count
            </button>
            <div class="m-2 ml-5 font-semibold"> {{ countRequest}} request made.</div>
            <input class="mx-5" v-model="name" placeholder="Set Your name">
            <button v-on:click="setName(name)" class="bg-transparent hover:bg-green-500 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-500 hover:border-transparent rounded float-right">
                Set Name
            </button>

          </div>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <!-- Replace with your content -->
      <div class="px-4 py-6 sm:px-0">
        <div class="border-4 border-solid border-gray-200 rounded-lg">
          <div class="flex flex-row border-2 border-gray-100 p-2 m-auto bg-white shadow-lg">
            <div class="m-2 w-4 font-semibold"> Code</div>
            <div class="my-2 ml-5 w-5/6 text-center text-red-600 font-semibold"> Unresolved Error</div>
          </div>
        </div>
        <div class="border-4 border-solid border-gray-200 rounded-lg  overflow-y-scroll scrolling-touch" v-bind:class="{'h-auto':(unresolved.length < 10 ? true : false), 'h-full':(unresolved.length > 10 ? true : false)}">
          <div v-if="unresolved.length>0">
          <!-- Unresolved: -->
            <div v-for="(error,idx) in unresolved" :key="error.index" class="bg-white even:bg-gray-200">
              <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
                <!-- <span class="flex rounded-full bg-green-500 uppercase px-2 py-0 text-xs font-bold m-auto h-auto justify-start">Resolved</span> -->
                <div class="m-2 w-4">{{ error.code }}</div>  
                <div class="m-2 w-4/6"> {{ error.text }}</div>
                <div>
                  
                  <!-- if it was added from other list -->
                  <button v-if="error.undo" v-on:click="undoChange(error.prevArr, 'unresolved',error.index,idx)" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded float-right ml-3">
                    Undo
                  </button>
                  <button v-else v-on:click="changeError('unresolved',idx)" class="bg-transparent hover:bg-green-500 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-500 hover:border-transparent rounded float-right">
                      Mark as resolved
                  </button>
                  <!-- For backlog errors -->
                  <button v-if="error.isbacklog" v-on:click="changeError('unresolved',idx)" class="bg-transparent hover:bg-green-500 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-500 hover:border-transparent rounded float-right">
                      Mark as resolved
                  </button>
                </div>
              </div>

            </div>
          </div>
          <div v-else>
            <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
              <div class="m-2 text-center text-green-700 font-semibold">Great job you have fixed these errors. Make sure even the backlogs are fixed.</div> 
            </div>
          </div>
        </div>
        <div class="border-4 border-solid border-gray-200 rounded-lg  mt-10">
          <div class="flex flex-row border-2 border-gray-100 p-2 m-auto bg-white shadow-lg">
            <div class="m-2 w-4 font-semibold"> Code</div>
            <div class="my-2 ml-5 w-5/6 text-center text-green-600 font-semibold"> Resolved Error</div>
          </div>
        </div>
        <div class="border-4 border-solid border-gray-200 rounded-lg overflow-y-scroll scrolling-touch" v-bind:class="{'h-auto':(resolved.length < 10 ? true : false), 'h-full':(resolved.length > 10 ? true : false)}">
        <div  v-if="resolved.length>0">
            <!-- Resolved:  -->
            <div v-for="(error,idx) in resolved" :key="error.index">
              <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
                <div class="m-2 w-4">{{ error.code }}</div>  
                <div class="m-2 w-4/6"> {{ error.text }}</div>
                <div>
                  <!-- if it was added from other list -->
                  <button v-if="error.undo" v-on:click="undoChange(error.prevArr, 'resolved',error.index,idx)" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded float-right ml-3">
                    Undo
                  </button>
                  <button v-else v-on:click="changeError('resolved',idx)" class="bg-transparent hover:bg-red-500 text-red-700 font-semibold hover:text-white py-2 px-4 border border-red-500 hover:border-transparent rounded ">
                    Mark as Unresolved
                  </button>
                  
                </div>
              </div>
            </div>
          </div>
          <div v-else>
            <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
              <div class="m-2 text-center text-red-700 font-semibold">Oh no! we need to catch up to fix the errors.</div> 
            </div>
          </div>
        </div>
        
        <div class="border-4 border-solid border-gray-200 rounded-lg mt-10">
          <div class="flex flex-row border-2 border-gray-100 p-2 m-auto bg-white shadow-lg">
            <div class="m-2 w-4 font-semibold"> Code</div>
            <div class="my-2 ml-5 w-5/6 text-center text-blue-600 font-semibold"> Backlog Error</div>
          </div>
        </div>
        <div class="border-4 border-solid border-gray-200 rounded-lg overflow-y-scroll scrolling-touch" v-bind:class="{'h-auto':(resolved.length < 10 ? true : false), 'h-full':(backlog.length > 10 ? true : false)}">
            <div  v-if="backlog.length>0">
              <!-- Backlog: -->
              <div v-for="(error,idx) in backlog" :key="error.index">
                <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
                <div class="m-2 w-4">{{ error.code }}</div>  
                <div class="m-2 w-4/6"> {{ error.text }}</div>
                <div>
                  <button v-on:click="changeError('backlog',idx)" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded float-right">
                    Mark as Unresolved
                  </button>
                </div>
                </div>
              </div>
            </div>
            <div v-else>
            <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
              <div class="m-2 text-center text-green-700 font-semibold">Great job you have fixed these errors. Make sure even the unresolved are fixed.</div> 
            </div>
          </div>
        </div>
      </div>
      <!-- /End replace -->
    </div>
  </main>

  

</div>
</template>


<script>
export default {
  async asyncData({ $axios }) {
    try {
      let { resolved, unresolved, backlog } = await $axios.$get(
        "http://localhost:8000/get_lists"
      );
      return {
        resolved,
        unresolved,
        backlog
      };
    } catch (error) {
      console.log(
        `Couldn't get error lists:\n${error}\nDid you start the API?`
      );
      console.log(
        "HINT: You can comment out thes full `asyncData` method and work with mocked data for UI/UX development, if you want to."
      );
    }
  },
  data() {
    return {

      resolved: [],
      unresolved: [],
      backlog: [],
      templateBox: [],
      backlogidx: [],
      isOpen: false,
      countRequest:0,
      notificationlist: [],
      showNotification:false,
      name: null

    };
  },
  created(){
    //collect all backlog indexes which we use in future for undoing
    this.collectBacklogIdx();
  },
  methods: {
    collectBacklogIdx: function(){
      for(var i = 0; i< this.backlog.length;i++){
        this.backlogidx.push(this.backlog[i].index);
      }
    },
    changeError: function (typeError,idx) {
      //changeError gets triggered when change error btn is clicked
      // console.log("this was entered",typeError,idx);

      //create template object to be pushed to new list
      this.createTemplate(typeError,idx,true);
      if (typeError == 'unresolved'){
        //add to notification list
        this.addNotification(typeError,'resolved',this.templateBox[0].index)
        this.pushToArray('unresolved','resolved');
      }
      else{
        this.addNotification(typeError,'unresolved',this.templateBox[0].index)
        this.pushToArray(typeError,'unresolved');
      }
      // send notification
      // this.showLoginError({message: "hey"})

      //remove the source array once pushed to new array
      this.spliceList(typeError,idx);


    },
    pushToArray: function (sourceList,destList){
      /**destArray to which array is the error code pushed to
      unresolved (sourceList) -> resolved (destList)
      undoVal to set undoval whther we are marking it or undoing it**/
      if(destList=='resolved'){
        // query came from unresolved
        this.resolved.push({
        index:    this.templateBox[0].index,
        code:     this.templateBox[0].code,
        text:     this.templateBox[0].text,
        prevArr:  'unresolved', 
        undo :    this.templateBox[0].undo,
        isbacklog:this.isExist(this.templateBox[0].index)
      })
      }
      else if(destList == 'unresolved' && sourceList =='resolved'){
        //query is for unresolved and came from resolve list
        var preArrVal = this.isExist(this.templateBox[0].index)? 'backlog' :'resolved';
        this.unresolved.push({
        index:    this.templateBox[0].index,
        code:     this.templateBox[0].code,
        text:     this.templateBox[0].text,
        prevArr:  preArrVal, 
        undo :    this.templateBox[0].undo,
        isbacklog:this.isExist(this.templateBox[0].index)
      })
      }
      else if(destList == 'unresolved' && sourceList =='backlog'){
        //query is for unreolved and came from resolve list
        this.unresolved.push({
        index:    this.templateBox[0].index,
        code:     this.templateBox[0].code,
        text:     this.templateBox[0].text,
        prevArr:  'backlog', 
        undo :    this.templateBox[0].undo,
        isbacklog:this.isExist(this.templateBox[0].index)
      })
      }
      
      this.templateBox.pop();
      // console.log(this.resolved);

    },
    undoChange: function(prevArr, currentArr, errorID, idx){
      // console.log(prevArr,currentArr,"lets change this",errorID,idx);
      if(prevArr=='unresolved'){
        //only values from resolved can be undone to unresolve
        var undoVal = this.isExist(this.resolved[idx].index) ? true : false ;
        this.createTemplate(currentArr,idx, undoVal);
        if (undoVal){
          //we are not setting prevall value for backlogs
          this.templateBox[0].prevArr = 'backlog';
        }

        //find the closest element is list while undoing
        var closest = this.getClosest('unresolved',this.resolved[idx].index);
        //add to unresolved list
        this.unresolved.splice(closest,0,this.templateBox[0]);
        
      }
      else if(prevArr=='resolved'){
        var undoVal = this.isExist(this.unresolved[idx].index) ? true : false ;
        this.createTemplate(currentArr,idx, undoVal);
        var closest = this.getClosest('resolved',this.unresolved[idx].index);
        this.resolved.splice(closest,0,this.templateBox[0]);
      }
      else if(prevArr=='backlog'){
        var undoVal = this.isExist(this.unresolved[idx].index) ? true : false ;
        this.createTemplate(currentArr,idx, undoVal);
        var closest = this.getClosest('backlog',this.unresolved[idx].index);
        this.backlog.splice(closest,0,this.templateBox[0]);
      }
      this.spliceList(currentArr,idx);
    },
    getClosest: function(arrToCheck, idx){
      /** while undoing the changes we need to put the object in its previous list where is belongs for that we try to find the closest index in that list for the object 
      arrToCheck -> previous list to be checked for undoing
      idx -> original index of the object when it was present in that list**/
      if (arrToCheck=='unresolved'){
        for(var i =0; i < this.unresolved.length; i++){
          if(Math.abs(this.unresolved[i].index)>idx){
            return i;break;
          }
        }
        //if last element was selected since loop wont enter this length.
        return this.unresolved.length;
      }
      else if (arrToCheck=='resolved'){
        for(var i =0; i < this.resolved.length; i++){
          if(Math.abs(this.resolved[i].index)>idx){
            return i;break;
          }
        }
        //if last element was selected since loop wont enter this length.
        return this.resolved.length;
      }
      else if (arrToCheck=='backlog'){
        for(var i =0; i < this.backlog.length; i++){
          if(Math.abs(this.backlog[i].index)>idx){
            return i;break;
          }
        }
        //if last element was selected since loop wont enter this length.
        return this.backlog.length;
      }
      //end of if elseif
    },
    createTemplate: function(sourceArr,idx,undoVal){
    /** Function creates object which needs to be transfered **/
    /** sourceArr -> object to be copied from
        idx -> index of the objec **/
      this.templateBox.pop(); // empty templatebox
      try {
        if(sourceArr=='unresolved'){
          this.templateBox.push({
            index: this.unresolved[idx].index,
            code: this.unresolved[idx].code,
            text: this.unresolved[idx].text,
            undo: undoVal,
            isbacklog: this.isExist(this.unresolved[idx].index)
          })
        }
        else if(sourceArr=='resolved'){
          this.templateBox.push({
            index: this.resolved[idx].index,
            code: this.resolved[idx].code,
            text: this.resolved[idx].text,
            undo: undoVal,
            isbacklog: this.isExist(this.resolved[idx].index)
          })
        }
        else if(sourceArr=='backlog'){
          this.templateBox.push({
            index: this.backlog[idx].index,
            code: this.backlog[idx].code,
            text: this.backlog[idx].text,
            undo: undoVal,
            isbacklog: this.isExist(this.backlog[idx].index)
          })
        }
      }catch (error) {
        console.log("Please check your source array something went wrong.");
      }
    },
    spliceList: function(sourceArr,idx){
      /** to remove the object from list when its status has changed
      // sourceArr -> list from which object to be removed
        idx-> index of the object in the list
      **/
      if(sourceArr == 'unresolved'){
        this.unresolved.splice(idx,1);
      }
      else if(sourceArr == 'resolved'){
        this.resolved.splice(idx,1);
      }
      else if(sourceArr == 'backlog'){
        this.backlog.splice(idx,1);
      }
    },
    isExist: function(idx){
      for(var i =0; i < this.backlogidx.length; i++){
        if(Math.abs(this.backlogidx[i]) == Math.abs(idx)){
          return true;
          break;
        }
    }
    return false
  },
  async getCount(){
    try {
      const countData = await this.$axios.$get('http://localhost:8000/get_log_count',{ crossdomain: true })
      this.countRequest = countData[0]
    } catch (error) {
      console.log(
        `Couldn't get count :\n${error}\nDid you start the API?`
      );
    }
  },
  addNotification: function(sourceArr,destArr,idx){
    this.notificationlist.push({
      index:this.notificationlist.length,
      text:"Error code "+idx+" was moved from "+sourceArr+" to "+destArr,
      timestamp: new Date()
    })
  },
  async setName(name){
    this.name = name;
    var data = {
      uname: this.name
    }
    try {
      const nameData = await this.$axios.$post('http://localhost:8000/setname', data,{ crossdomain: true })
      console.log(nameData);
    } catch (error) {
      console.log(
        `Couldn't set name :\n${error}\nDid you start the API?`
      );
    }
  }

},
notifications: {
      showLoginError:{ // You can have any name you want instead of 'showLoginError'
        title: 'Test ',
        message: 'Failed to notify',
        type: 'warn' // You also can use 'VueNotifications.types.error' instead of 'error'
      }
 }
};


</script>
