<template>
    <vs-button vs-type="filled">Hello World</vs-button>
</template>
  
 <script>
     import axios from 'axios';
     import Vuesax from 'vuesax';
     export default {
     name: 'Login',
     data() {
         return {
         Login: '',
         Password: '',
         data: [],
         };
 
     }
     }
 </script>
 
 <style>
     @import '../assets/css/main.css';
     @import '../assets/css/font.css';
 </style>