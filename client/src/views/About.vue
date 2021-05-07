<!--About.vue-->
<template>
  <h2>About</h2>
  <p>{{ msg }}</p>
  <p>{{ msg2 }}</p>
  <router-link to='/'>Back</router-link>
</template>

<script>
import axios from 'axios'

export default {
  name: 'About',
  data() {
    return {
      msg: '',
      msg2: ''
    }
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/flask';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getMessage2() {
      const path = 'http://localhost:5000/test';
      axios.get(path)
        .then((res) => {
          this.msg2 = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
    this.getMessage2();
  }
}
</script>