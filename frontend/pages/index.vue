<template>
  <!-- <script src="https://cdn.jsdelivr.net/npm/vue@2.6.11"></script> -->
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
            <button class="p-1 border-2 border-transparent text-gray-400 rounded-full hover:text-white focus:outline-none focus:text-white focus:bg-gray-700" aria-label="Notifications">
              <!-- <svg class="h-6 w-6" stroke="currentColor" fill="none" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
              </svg> -->
            </button>

            <!-- Profile dropdown -->
            <div class="ml-3 relative">
              <div>
                <button class="max-w-xs flex items-center text-sm rounded-full text-white focus:outline-none focus:shadow-solid" id="user-menu" aria-label="User menu" aria-haspopup="true">
                  <img class="h-8 w-8 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
                </button>
              </div>
              <!--
                Profile dropdown panel, show/hide based on dropdown state.

                Entering: "transition ease-out duration-100"
                  From: "transform opacity-0 scale-95"
                  To: "transform opacity-100 scale-100"
                Leaving: "transition ease-in duration-75"
                  From: "transform opacity-100 scale-100"
                  To: "transform opacity-0 scale-95"
              -->
              <div class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg">
                <div class="py-1 rounded-md bg-white shadow-xs" role="menu" aria-orientation="vertical" aria-labelledby="user-menu">
                  <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Your Profile
                  </a>
                  <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Settings
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
      <div class="pt-4 pb-3 border-t border-gray-700">
        <div class="flex items-center px-5">
          <div class="flex-shrink-0">
            <img class="h-10 w-10 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
          </div>
          <div class="ml-3">
            <div class="text-base font-medium leading-none text-white">Tom Cook
            </div>
            <div class="mt-1 text-sm font-medium leading-none text-gray-400">tom@example.com
            </div>
          </div>
        </div>
        <div class="mt-3 px-2">
          <a href="#" class="block px-3 py-2 rounded-md text-base font-medium text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Your Profile
          </a>
          <a href="#" class="mt-1 block px-3 py-2 rounded-md text-base font-medium text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Settings
          </a>
          <a href="#" class="mt-1 block px-3 py-2 rounded-md text-base font-medium text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:text-white focus:bg-gray-700">Sign out
          </a>
        </div>
      </div>
    </div>
  </nav>

  <header class="bg-white shadow">
    <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold leading-tight text-gray-900">
        Dashboard
      </h1>
    </div>
  </header>
  <main>

    <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <!-- Replace with your content -->
      <div class="px-4 py-6 sm:px-0">
        <div class="border-4 border-solid border-gray-200 rounded-lg h-screen overflow-y-scroll scrolling-touch">
          <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
            <div class="m-2 w-4"> Code</div>
            <div class="my-2 ml-5 w-5/6 text-center"> Error</div>
          </div>
          <div>
          <!-- Unresolved: -->
            <div v-for="(error,idx) in unresolved" :key="error.index" class="bg-white even:bg-gray-200">
              <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
                <!-- <span class="flex rounded-full bg-green-500 uppercase px-2 py-0 text-xs font-bold m-auto h-auto justify-start">Resolved</span> -->
                <div class="m-2 w-4">{{ error.code }}</div>  
                <div class="m-2 w-4/6"> {{ error.text }}{{ idx }} {{ error.index }}</div>
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
        </div>
        <div class="border-4 border-solid border-gray-200 rounded-lg h-screen overflow-y-scroll scrolling-touch">
        <div>
            <!-- Resolved:  -->
            <div v-for="(error,idx) in resolved" :key="error.index">
              <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
                <div class="m-2 w-4">{{ error.code }}</div>  
                <div class="m-2 w-4/6"> {{ error.text }} {{ idx }} {{ error.index }}</div>
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
        </div>
        <div class="border-4 border-solid border-gray-200 rounded-lg h-screen overflow-y-scroll scrolling-touch">
            <div>
              <!-- Backlog: -->
              <div v-for="(error,idx) in backlog" :key="error.index">
                <div class="flex flex-row border-2 border-gray-100 p-2 h-auto m-auto bg-white shadow-lg  overflow-hidden">
                <div class="m-2 w-4">{{ error.code }}</div>  
                <div class="m-2 w-4/6"> {{ error.text }} {{ idx }} {{ error.index }}</div>
                <div>
                  <button v-on:click="changeError('backlog',idx)" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded float-right">
                    Mark as Unresolved
                  </button>
                </div>
                </div>
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
      backlogidx: []

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
        this.pushToArray('unresolved','resolved');
      }
      else{
        this.pushToArray(typeError,'unresolved');
      }
      
      // console.log(this.unresolved,this.resolved,this.backlog)
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
  }
}
};


</script>
