<template>
    

<div id="editor">
  <textarea :value="input" @input="update"></textarea>
  <div v-html="compiledMarkdown"></div>
</div>


  </template>
  
  <script>
  import marked from 'marked';
  import _ from 'lodash';
  
  export default {
    data() {
      return {
        input: '# hello'
      };
    },
    computed: {
      compiledMarkdown() {
        return marked(this.input, { sanitize: true });
      }
    },
    methods: {
      update: _.debounce(function(e) {
        this.input = e.target.value;
      }, 300)
    }
  };
  </script>

<style>
textarea {
  border-color: rgb(106, 78, 147);
  border-radius: 10px;
  overflow: auto;
  outline: none;

  -webkit-box-shadow: none;
  -moz-box-shadow: none;
  box-shadow: none;

  resize: none;
}
</style>