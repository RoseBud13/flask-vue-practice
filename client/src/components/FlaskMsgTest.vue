<template>
  <div>
      <p>{{ msg }}</p>
      <p>{{ MsgFromFlask }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'FlaskMsgTest',
  data() {
      return {
          msg: 'Message from Vue',
          MsgFromFlask: ''
      }
  },
  methods: {
      const path = 'http://localhost:5000/flask';
      getMessageFromFlask() {
          axios.get(path)
          .then((res) => {
              this.MsgFromFlask = res.data;
          })
          .catch((error) => {
              console.error(error);
          });
      }
  },
  created() {
      this.getMessageFromFlask();
  }
}
</script>

<style>

</style>