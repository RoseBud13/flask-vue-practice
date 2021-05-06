<!--Home.vue-->
<template>
  <img alt="Vue logo" src="../assets/logo.png" />
  <HelloWorld msg="Hello Vue 3 + Vite" />
  <router-link to='/about'>About</router-link>
</template>

<script>
import HelloWorld from '../components/HelloWorld.vue'

export default {
  name: 'Home',
  components:{
      HelloWorld
  }
}
</script>