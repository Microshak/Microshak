<template>

  <div class="hello">
        <link href='https://fonts.googleapis.com/css?family=Terminal+Dosis' rel='stylesheet' type='text/css' />

               
    <div class="name zoomOut  animated">
    <p class="trns-text M">M</p>
    <p class="trns-text I">I</p>
    <p class="trns-text C">C</p>
    <p class="trns-text R">R</p>
    <p class="trns-text O">O</p>
    <p class="trns-text S">S</p>
    <p class="trns-text H">H</p>
    <p class="trns-text A">A</p>
    <p class="trns-text K">K</p>
    
       </div>
    <div>
      <a href="https://medium.com/@microshak" class="menu1">BLOG</a>

    </div>



  
 <ul class="ca-menu" style="display:none;">
                    <li>
                        <a href="https://medium.com/@microshak">
                            <span class="ca-icon">F</span>
                            <div class="ca-content">
                                <h2 class="ca-main">Blog</h2>
                                <h3 class="ca-sub">Teaching</h3>
                            </div>
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <span class="ca-icon">H</span>
                            <div class="ca-content">
                                <h2 class="ca-main">Publications</h2>
                                <h3 class="ca-sub">Advanced use of technology</h3>
                            </div>
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <span class="ca-icon" id="heart">N</span>
                            <div class="ca-content">
                                <h2 class="ca-main">Infographical Education</h2>
                                <h3 class="ca-sub">Understanding visually</h3>
                            </div>
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <span class="ca-icon">K</span>
                            <div class="ca-content">
                                <h2 class="ca-main">Sophisticated Team</h2>
                                <h3 class="ca-sub">Professionals in action</h3>
                            </div>
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <span class="ca-icon">L</span>
                            <div class="ca-content">
                                <h2 class="ca-main">Unconditional Support</h2>
                                <h3 class="ca-sub">24/7 for you needs</h3>
                            </div>
                        </a>
                    </li>
                </ul>


  </div>


  
</template>
<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  mouseMove(){

  },
    created() {
 
 const url = new URL('../assets/img/rock.mp3', import.meta.url).href
console.log(url)

 

  },
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

:root:before {
  content: url(../assets/img/plaines.jpg)
           url(../assets/img/MikeGermany2.jpg)
           url(../assets/img/Adorable.jpg)
           url(../assets/img/MikeGermany.jpg)
               url(../assets/img/glasses.jpg)
                   url(../assets/img/duck.jpg);
   
}

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

.M { animation: changeM 0.9s infinite;
     
       background-repeat: no-repeat;
         -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}

@keyframes changeM{
0%,100%{
  background: url(../assets/img/plaines.jpg)  ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  background-repeat: no-repeat;
   background-size: 500px 800px;
}

33% {background: url(../assets/img/MikeGermany2.jpg)    no-repeat;
  background-size: 500px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}

66% {background: url(../assets/img/Adorable.jpg)    no-repeat;
  background-size: 500px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}}


.I {animation: changeI 0.95s infinite;
    background: url(../assets/img/MikeGermany.jpg)    no-repeat;
    background-size: 140% !important;
        background-position: -55px 50%;
}

@keyframes changeI{
0%,100%{
  background: url(../assets/img/glasses.jpg)  ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  background-repeat: no-repeat;
   background-size: 500px 800px;
}

33% {background: url(../assets/img/duck.jpg)    no-repeat;
  background-size: 500px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}

66% {background: url(../assets/img/cap.jpg)    no-repeat;
  background-size: 500px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}}


.C {animation: changeC 0.91s infinite;
    background: url(../assets/img/kids.jpg)   -20px -20px no-repeat;
    background-position: 66% 75%;
     background-size: 3% 10px;
       background-repeat: no-repeat;
}

@keyframes changeC{
0%,100%{
  background: url(../assets/img/glasses.jpg)  ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  background-repeat: no-repeat;
   background-size: 500px 800px;
}

33% {background: url(../assets/img/mikeChrissy.jpg)    no-repeat;
  background-size: 500px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}

66% {background: url(../assets/img/tween.jpg)    no-repeat;
  background-size: 500px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}}


.R {animation: changeR 0.91s infinite;
    background: url(../assets/img/kids.jpg)   -20px -20px no-repeat;
    background-position: 66% 75%;
     background-size: 3% 10px;
       background-repeat: no-repeat;
}

@keyframes changeR{
0%,100%{
  background: url(../assets/img/babyz.JPG)  ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  background-repeat: no-repeat;
   background-size: 800px 800px ;
}

33% {background: url(../assets/img/ChristmasInHaitti.jpg)    no-repeat;
  background-size:800px 800px ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}

66% {background: url(../assets/img/pfam.jpg)    no-repeat;
  background-size:  800px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}}


.O {animation: changeO 0.81s infinite;
    background: url(../assets/img/kids.jpg)   -20px -20px no-repeat;
    background-position: 66% 75%;
     background-size: 3% 10px;
       background-repeat: no-repeat;
}

@keyframes changeO{
0%,100%{
  background: url(../assets/img/hike.jpg)  ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  background-repeat: no-repeat;
   background-size: 800px 800px ;
}

33% {background: url(../assets/img/Peace.jpg)    no-repeat;
  background-size:800px 800px ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}

66% {background: url(../assets/img/tot.jpg)    no-repeat;
  background-size:  800px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}}

.S {animation: changeS 0.81s infinite;
    background: url(../assets/img/kids.jpg)   -20px -20px no-repeat;
    background-position: 66% 75%;
     background-size: 3% 10px;
       background-repeat: no-repeat;
}

@keyframes changeS{
0%,100%{
  background: url(../assets/img/bacl.jpg)  ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  background-repeat: no-repeat;
   background-size: 500px 800px ;
}

33% {background: url(../assets/img/candy.JPG)    no-repeat;
  background-size:500px 800px ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}

66% {background: url(../assets/img/DadAndGrandpa.jpg)    no-repeat;
  background-size:  500px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}}



.H {animation: changeH 0.81s infinite;
    background: url(../assets/img/kids.jpg)   -20px -20px no-repeat;
    background-position: 66% 75%;
     background-size: 3% 10px;
       background-repeat: no-repeat;
}

@keyframes changeH{
0%,100%{
  background: url(../assets/img/miketillers.jpg)  ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  background-repeat: no-repeat;
   background-size: 500px 800px ;
}

33% {background: url(../assets/img/tot.jpg)    no-repeat;
  background-size:500px 800px ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}

66% {background: url(../assets/img/ChiMike.jpg)    no-repeat;
  background-size:  500px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}}


.A {animation: changeA 0.881s infinite;
    background: url(../assets/img/duck.jpg)   -20px -20px no-repeat;
    background-position: 66% 75%;
     background-size: 3% 10px;
       background-repeat: no-repeat;
}

@keyframes changeA{
0%,100%{
  background: url(../assets/img/famz.jpg)  ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  background-repeat: no-repeat;
   background-size: 500px 800px ;
}

33% {background: url(../assets/img/cnm.jpg)    no-repeat;
  background-size:500px 800px ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}

66% {background: url(../assets/img/fall.jpg)    no-repeat;
  background-size:  500px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}}


.K {animation: changeK 0.7s infinite;
    background: url(../assets/img/duck.jpg)   -20px -20px no-repeat;
    background-position: 66% 75%;
     background-size: 3% 10px;
       background-repeat: no-repeat;
}

@keyframes changeK{
0%,100%{
  background: url(../assets/img/train.jpg)  ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  background-repeat: no-repeat;
   background-size: 500px 800px ;
}

33% {background: url(../assets/img/ban.jpg)    no-repeat;
  background-size:500px 800px ;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}

66% {background: url(../assets/img/color.jpg)    no-repeat;
  background-size:  500px 800px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}}






.trns-text  {

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
  filter: drop-shadow(0px 0px 7px rgba(150, 150, 150, .7));
}







/*base code*/

.animated {
  -webkit-animation-duration: 20s;
  animation-duration: 20s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}

.animated.infinite {
  -webkit-animation-iteration-count: infinite;
  animation-iteration-count: infinite;
}

.animated.hinge {
  -webkit-animation-duration: 110s;
  animation-duration: 110s;
}




/*the animation definition*/
.zoomOut {
   transform: rotate(0deg);
  position: absolute;
  animation-iteration-count:1;
animation-name:zoomOut;
animation-delay: 5s;
animation-fill-mode: forwards;
-webkit-animation-fill-mode: forwards;
  animation:  zoomOut 9s    ;
   top:-38vh;
      opacity: 1;
    -webkit-transform: scale3d(.05, .05, .05);
    -ms-transform: scale3d(.05, .05, .05);
    transform: scale3d(.10, .1, .1);
left:0px;
z-index: 100;
}


@keyframes zoomOut {
  0% {
    opacity: 1;
    -webkit-transform: scale3d(30, 30, 30);
    -ms-transform: scale3d(30, 30, 30);
    transform: scale3d(30, 30, 30);
     top:-0vh;
    
      
  }



  70% {
     opacity: 1;
    -webkit-transform: scale3d(.3, .3, .3);
    -ms-transform: scale3d(.3, .3, .3);
    transform: scale3d(.5, .5, .5);
  top:20vh;
  
  }

  98% {
    opacity: 1;
    -webkit-transform: scale3d(.7, .7, .7);
    -ms-transform: scale3d(.7, .7, .7);
    transform: scale3d(.2, .2, .2);
    top:-30vh;
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(.01, .01, .01);
    -ms-transform: scale3d(.01, .01, .01);
    transform: scale3d(.10, .1, .1);
    top:-38vh;

  }
}
@keyframes move {
  0% {
      
      
  }

    20% {
   
      
  }
  50% {
     transform: rotate(0deg);
  }


}





.menu1 {
  position:relative;
  color:white;
  font-size: 2.4vw;
  animation: slidei 2s 1    ;
animation-delay: 10s;
animation-fill-mode: forwards;
opacity: 0;
transition-timing-function: ease-in-out;
top:0vh;
margin-left:8vw;
font-family: 'Verdana';
text-decoration: none;;
}

@keyframes slidei {
   from {left: 20vh;opacity:0;
   
  text-shadow: 0 0 0px #fff, 0 0 0px #fff, 0 0 0px #02020a, 0 0 0px #02020a, 0 0 0px #02020a, 0 0 0px #02020a, 0 0 0px #02020a;
 
   }

   95% {left: 25vh;opacity:1;
   
      text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #02020a, 0 0 40px #02020a, 0 0 50px #02020a, 0 0 60px #02020a, 0 0 70px #02020a;
 
   }
         97% {left: 25vh;opacity:1;
   
      text-shadow: 0 0 50px #fff, 0 0 60px #fff, 0 0 70px #02020a, 0 0 80px #02020a, 0 0 90px #02020a, 0 0 100px #02020a, 0 0 110px #02020a;
 
   }

      99% {left: 25vh;opacity:1;
   
      text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #02020a, 0 0 40px #02020a, 0 0 50px #02020a, 0 0 60px #02020a, 0 0 70px #02020a;
 
   }
  to {left: 25vh;
  opacity:1;
     text-shadow: 0 0 1px #fff, 0 0 2px #fff, 0 0 3px #02020a, 0 0 4px #02020a, 0 0 5px #02020a, 0 0 6px #02020a, 0 0 7px #02020a;
 
  }
}


.glow {
  animation: glow 1s ease-in-out infinite alternate;

}

@-webkit-keyframes glow {
  from {
    text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #02020a, 0 0 40px #02020a, 0 0 50px #02020a, 0 0 60px #02020a, 0 0 70px #02020a;
  }
  
  to {
    text-shadow: 0 0 20px #fff, 0 0 30px #ff4da6, 0 0 40px #ff4da6, 0 0 50px #ff4da6, 0 0 60px #ff4da6, 0 0 70px #ff4da6, 0 0 80px #ff4da6;
  }
}



/*menu https://tympanus.net/Tutorials/CreativeCSS3AnimationMenus/index10.html*/

.ca-menu{
  
    padding: 0 0 0 48px;
    margin: 200px,1000px, 0,0;
    width: 1020px;
    
  
}
.ca-menu li{
    width: 230px;
    height: 230px;
    border: 10px solid #f6f6f6;
    overflow: hidden;
    position: relative;
    float:left;
    background: #fff;
    margin-left:-48px;
    margin-top:400px;
    -webkit-box-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    -moz-box-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    box-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    -webkit-border-radius: 125px;
    -moz-border-radius: 125px;
    border-radius: 125px;
    -webkit-transition: all 400ms linear;
    -moz-transition: all 400ms linear;
    -o-transition: all 400ms linear;
    -ms-transition: all 400ms linear;
    transition: all 400ms linear;
    z-index: 20;
}
.ca-menu li:last-child{
    margin-right: 0px;
}
.ca-menu li a{
    text-align: left;
    width: 100%;
    height: 100%;
    display: block;
    color: #333;
    position: relative;
}
.ca-icon{
    font-family: 'WebSymbolsRegular', cursive;
    font-size: 40px;
    color: #f6f6f6;;
    line-height: 60px;
    position: absolute;
    width: 100%;
    height: 60px;
    left: 0px;
    top: 30px;
    text-align: center;
    -webkit-transition: all 400ms linear;
    -moz-transition: all 400ms linear;
    -o-transition: all 400ms linear;
    -ms-transition: all 400ms linear;
    transition: all 400ms linear;
}
.ca-main{
    font-size: 24px;
    position: absolute;
    top: 110px;
    height: 80px;
    width: 170px;
    left: 50%;
    margin-left: -85px;
    opacity: 0.8;
    text-align: center;
    color: #555;
}
.ca-sub{
    display: none;
}
.ca-menu li:hover{
    border-color: #333;
    z-index: 999;
    -webkit-transform: scale(1.1);
    -moz-transform: scale(1.1);
    -o-transform: scale(1.1);
    -ms-transform: scale(1.1);
    transform: scale(1.1);
}
.ca-menu li:hover .ca-icon{
    color: #000;
    font-size: 60px;
    text-shadow: 0px 0px 1px #000;
    -webkit-animation: moveFromBottom 300ms ease;
    -moz-animation: moveFromBottom 300ms ease;
    -ms-animation: moveFromBottom 300ms ease;
}
.ca-menu li:hover .ca-main{
    color: #000;
    -webkit-animation: moveFromBottom 500ms ease;
    -moz-animation: moveFromBottom 500ms ease;
    -ms-animation: moveFromBottom 500ms ease;
}

@-webkit-keyframes moveFromBottom {
    from {
        -webkit-transform: translateY(200%) scale(0.5);
        opacity: 0;
    }
    to {
        -webkit-transform: translateY(0%) scale(1);
        opacity: 1;        
    }
}
@-moz-keyframes moveFromBottom {
    from {
        -moz-transform: translateY(200%) scale(0.5);
        opacity: 0;
    }
    to {
        -moz-transform: translateY(0%) scale(1);
        opacity: 1;        
    }
}
@-ms-keyframes moveFromBottom {
    from {
        -ms-transform: translateY(200%) scale(0.5);
        opacity: 0;
    }
    to {
        -ms-transform: translateY(0%) scale(1);
        opacity: 1;        
    }
}


</style>
