<template>
  <div id="editor">
    <textarea :value="input" @input="update"></textarea>
    <div id="markdown-output">
      <div v-html="compiledMarkdown"></div>
    </div>
  </div>
  </template>
  
  <script>
  import marked from 'marked';
  import _ from 'lodash';
  
  export default {
    data() {
      return {
        input: '# Ваша история начинается тут'
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
#markdown-output {
  overflow: scroll;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  padding: 1vw;
}
#editor {
  margin: 0;
  height: 100%;
  font-family: "Helvetica Neue", Arial, sans-serif;
  color: #333;
  margin-top: 0px;
}

textarea,
#editor div {
  color: rgb(238, 239, 249);
  background-color: rgb(72, 72, 83);
  margin-top: 0px;
  display: inline-block;
  width: 49%;
  height: 100%;
  vertical-align: top;
  box-sizing: border-box;
  overflow-wrap: break-word;
  word-wrap: break-word;
  word-break: break-word;
}

textarea {
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  border: none;
  resize: none;
  outline: none;
  color: rgb(238, 239, 249);
  background-color: rgb(72, 72, 83);
  font-size: 1vw;
  font-family: "Monaco", courier, monospace;
  padding: 1vw;
}

code {
  color: #f66;
}

h1, h2, h3, h4, h5, h6 {
  margin-top: 1em;
  margin-bottom: 0.5em;
  font-weight: bold;
}

h1 {
  font-size: 2em;
}

h2 {
  font-size: 1.5em;
}

h3 {
  font-size: 1.17em;
}

h4 {
  font-size: 1em;
}

h5 {
  font-size: 0.83em;
}

h6 {
  font-size: 0.67em;
}

strong {
  font-weight: bold;
}

em {
  font-style: italic;
}

blockquote {
  margin: 1em 0;
  padding: 0.5em 1em;
  background-color: rgb(42, 42, 53);
  border-left: 2px solid #f66;
}

ol {
  margin: 1em 0;
  padding-left: 2em;
}

ul {
  margin: 1em 0;
  padding-left: 2em;
}

li {
  margin-bottom: 0.5em;
}

code {
  background-color: rgb(42, 42, 53);
  padding: 0.2em 0.4em;
  font-family: "Monaco", courier, monospace;
}

hr {
  border: none;
  border-top: 1px solid #f66;
  margin: 1em 0;
}
</style>