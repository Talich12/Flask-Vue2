<template>
    <div id="editor" class="container">
      <textarea :value="input" @input="update"></textarea>
      <div id="markdown-output" class="markdown-scroll">
        <span v-html="compiledMarkdown"></span>
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
      },
    },
    watch: {
      input: function(){
            this.$emit('body', {body: this.input})
      },
    },
    methods: {
      update: _.debounce(function(e) {
        this.input = e.target.value;
      }, 300)
    }
};
</script>

<style>
.container {
  display: flex;
  flex-direction: row;
  align-items: stretch;
  justify-content: space-between;
}

#markdown-output {
  overflow-y: scroll;
  z-index: 3;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  padding: 1vw;
  max-height: 75vh; /* Updated height */
  text-rendering: optimizeLegibility; /* Apply antialiasing to the text */
  box-shadow: 0px 5px 20px 0px rgba(0, 0, 0, var(--vs-shadow-opacity));
}

.markdown-scroll {
  overflow-wrap: break-word;
  word-wrap: break-word;
  z-index: 3;
  word-break: break-word;
}

#editor {
  margin: 0;
  height: 100vh;
  font-family: "Helvetica Neue", Arial, sans-serif;
  color: #333;
  z-index: 3;
  margin-top: 0px;
  opacity: 0.85;
}

textarea,
#editor div {
  color: rgb(238, 239, 249);
  background-color: rgb(72, 72, 83);
  margin-top: 0px;
  display: inline-block;
  width: 49%;
  height: 75vh; /* Updated height */
  vertical-align: top;
  box-sizing: border-box;
  overflow-wrap: break-word;
  z-index: 3;
  word-wrap: break-word;
  word-break: break-word;
}

#editor div {
  height: 100%;
  z-index: 3;
}

textarea {
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  border: none;
  resize: none;
  outline: none;
  z-index: 10;
  color: rgb(238, 239, 249);
  background-color: rgb(72, 72, 83);
  font-size: 1vw;
  font-family: "Monaco", courier, monospace;
  padding: 1vw;
  box-shadow: 0px 5px 20px 0px rgba(0, 0, 0, var(--vs-shadow-opacity));
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