
<template>
    <div class="center" style="height: 100%;">
      <vs-dialog scroll blur overflow-hidden not-close v-model="active" style="padding-top: 0; padding-bottom: 0;">
        <div class="storyheader" style="margin-bottom: 3vh; display: flex; align-items: center;">
          <vs-avatar>
          <img :src="require(`@/assets/img/load/${post_data.author.avatar}`)" alt="">
        </vs-avatar>
        <p style="font-size: 3vh; margin-left: 1vw;">{{ post_data.author.username }}</p>
        <vs-button
          v-if="post_data.has_video"
          color="#FF0000"
          border
          upload
          :activebtn="activebtn == 2"
          @click="active = 2"
          style="margin-left: 8vw;"
        >
          <i class="bx bxl-youtube"></i> Видео на youtube!
        </vs-button>
        <vs-button
          v-if="post_data.has_audio"
          danger
          border
          upload
          :activebtn="activebtn == 2" 
          @click="active = 2"
        >
          <i class="bx bxs-microphone-alt"></i> Озвучка истории!
        </vs-button>
        </div>
        <template #header>
          <h2>
            {{ post_data.title }}
          </h2>
        </template>
        <div class="con-content">
             <div v-html="markdownToHtml"></div>
        </div>
      </vs-dialog>
    </div>
  </template>

<script>
import marked from 'marked';
  export default {
    props: ['post_data', 'active'],
    data:() => ({
      activebtn: '',
      markdown:  `![cover](https://images.genius.com/8a661ac2b22e160af9e0504c29a0ffbc.1000x1000x1.png)
      # Текст песни "Отопление"

## [Куплет 1]
Когда солнышко отключит отопление  
Я обхвачу колени твои, чтоб не околели  
Так делают таёжники  
Я соберу тебя в комочек, ты поёрзаешь, поёрзаешь  
Но не замёрзнешь  

В храмах  
Толпы навьюченные хламом  
Топят горючим  
Толстые ляжки в тонких брючинах  
Нам их не жаль  
Солнце умрёт, крошась на ломтики:  
Каждому видимый упрёк: «Поделом тебе»  

Мы будем сторониться людей и схоронимся  
Под одеялом льда, нам опахалом лица  
Обнесёт ледяная мгла  
И в твои кудри пустит проседь снежную  
Я растоплю, если попросишь нежно  
В темноте, в коконе, что выткут ветра  
Я дам тебе с избытком тепла  

**Помни**: мне нужна лишь самая малость –  
Когда я буду замерзать, чтобы ты улыбалась  

## [Припев]
Я не знаю, как будет, и я не знаю, как быть  
Слепые руки обстоятельств нас задушат, как котят  
Давай скрутим в газету наш неустроенный быт  
Чтоб ты скурила, улыбаясь, как привыкла, не в затяг...

## [Куплет 2]
Когда, неаккуратно приняв опиаты
Господь в горячке опрокинет океаны
После уставится, сокрушаясь неистово, вниз –
Там, где-то меж полушарий, плот из половиц наш
Взлетит на лебёдке луна-акробат
Два ребёнка, пустой аквапарк
Кипит громада, меж волн горбатых
Ладони-вёсла сотни вёрст вяжут слепой фарватер
И на плоту – чёрной точкой в лазурной россыпи
Я заплету последней женской особи косы
И всё вокруг будет твоим
Даже акулий плавник
И ночь, что бури таит – всё
В часы, когда стихия давит глыбой монолитной
Скупой молитвой я буду сон хранить твой
Качаясь, словно маятник, умаявшись
Прильну к тебе
Пусть умирает мир – ты моя жизнь

[Припев]
Я не знаю, как будет, и я не знаю, как быть
Слепые руки обстоятельств нас задушат, как котят
Давай скрутим в газету наш неустроенный быт
Чтоб ты скурила, улыбаясь, как привыкла, не в затяг...

[Бридж]
Когда ЖЭК отключит отопление
Я обхвачу колени твои, чтоб не околели
Господь достанет укулеле, сядет у изголовья
Сыграет колыбельную, зыркая исподлобья
И твои глазки заколочены, и твои руки руками моими закавычены
Господь поймает бричку у обочины
И по делам укатит как обычно, как обычно...`,
    }),
    computed: {
        markdownToHtml(){
            return marked(this.$props.post_data.body);
        }
    }
}  
  </script>

<style>
.vs-dialog {
    background: #2A2A35;
    color: #EEEFF9;
}
.vs-dialog--scroll {
    max-width:none;
    width: 50vw;
    height: 100%;
    padding: 0;
    margin: 0;
}
.vs-dialog__content.notFooter {
    max-height: 100vh;
    height: 90vh;
    margin-bottom: 0;
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
img {
    max-width: 100%;
    height: auto;
}
</style>