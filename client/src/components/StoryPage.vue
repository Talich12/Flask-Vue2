
<template>
    <div class="center">
      <vs-button shadow @click="active=!active" style="left: 30%; z-index: 100;">
        Open Dialog
      </vs-button>
      <vs-dialog no-footer blur scroll overflow-hidden full-screen not-close v-model="active" style="padding-left: 12vw; padding-right: 12vw;">
        <template #header>
          <h3>
            ТУТ НАЗВАНИЕ ИСТОРИИ
          </h3>
        </template>
             <div v-html="markdownToHtml"></div>
      </vs-dialog>
    </div>
  </template>

<script>
import marked from 'marked';
  export default {
    data:() => ({
      active: false,
      markdown:  "# dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n # dsa *djsajdsa* \n",
    }),
    computed: {
        markdownToHtml(){
            return marked(this.markdown);
        }
    }
}  
  </script>

<style>
.vs-dialog--fullScreen {
    background: #2A2A35;
    color: #EEEFF9;
}
.vs-dialog__content .notFooter {
    height: 100%;
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