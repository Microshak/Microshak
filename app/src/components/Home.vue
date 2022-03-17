<template>
  <div class="hello">
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
        Microshak
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


    <div class="name">
    <p class="trns-text M">M</p>
    <p class="trns-text I">I</p>
    <p class="trns-text K">K</p>
    <p class="trns-text E">E</p>
    
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.name {
  display: flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  width: 100vw;
  height: calc(100vh - 60px);
}
.letter {
  margin: .8%;
  filter: drop-shadow(0px 0px 7px rgba(150, 150, 150, .7));
}
.letter-image {
  width: 100%;
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

.M {
    background: url(../assets/img/plaines.jpg)  ;
        background-position: 80% -50px;
     background-size: 3px 10px;
       background-repeat: no-repeat;
}


.I {
    background: url(../assets/img/MikeGermany.jpg)    no-repeat;
    background-size: 140% !important;
        background-position: -55px 50%;
}

.K {
    background: url(../assets/img/kids.jpg)   -20px -20px no-repeat;
    background-position: 66% 75%;
     background-size: 3% 10px;
       background-repeat: no-repeat;
}

.E {
    background: url(../assets/img/RobotMike.jpg)   -20px -20px no-repeat;
}

.trns-text {

  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  /* Below is not needed */
  display:block;
  font-size: 30vw;
  font-family: 'Verdana';
  text-align: center;
  margin-top: -20px;
  font-weight: bold;
  letter-spacing: -25px;
  background-size: cover;
  font-color:white;
  margin: .8%;
  filter: drop-shadow(0px 0px 7px rgba(150, 150, 150, .7));
}
</style>
