<template>
     <div class="menu">
      <div class="menu-item">
        <div class="menu-text">
          
        </div>
      </div>
      <div class="menu-item">
        <div class="menu-text">
          
        </div>
      </div>
      <div class="menu-item menu-center">
          <HelloWorld msg="Welcome to Your Vue.js App!!!!!"/>

      </div>
      <div class="menu-item">
        <div class="menu-text">
          
        </div>
      </div>
      <div class="menu-item">
        <div class="menu-text">
          
        </div>
      </div>
    </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: white;
  /* margin-top: 60px; */
  padding: 0;
  margin: 0;
}
body {
  background: #080808;
  padding: 0;
  margin: 0;
}

.menu {
  display: flex;
  align-items: center;
  justify-content: space-around;
  margin-top: 10px;
  height: 60px;
}

.menu-item {
  flex: 1;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.menu-text{
  font-size: 20px;
  color: #818181;
  cursor: pointer;
  padding: 10px;
  border-bottom: 2px solid #080808;
  width: fit-content;
}

.menu-text:hover {
  border-bottom: 2px solid #c278ff;
}

.menu-center {
  font-size: 36px;
  color: #EAEAEA;
}

</style>

