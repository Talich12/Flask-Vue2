<template>
    <div class="header">
        <img src="../assets/thrill.svg" alt="" class="image">
    </div>
  </template>
  
  <style>
  .header {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 10%;
    width: 100%;
    position: fixed;
    z-index: 2;
    top: 0;
    left: 0;
    background-color: #2A2A35;
    -webkit-box-shadow: 0 0 25px 0 rgba(0,0,0,0.4);
    -moz-box-shadow: 0 0 25px 0 rgba(0,0,0,0.4);
    box-shadow: 0 0 25px 0 rgba(0,0,0,0.4);
  }
  .image {
    height: 80%;
    margin-left: 14%;
  }
  .mask {
    height: 80%;
    margin-left: 14%;
    animation: rotate 2s infinite;
  }
  
    @keyframes rotate {
    0% {
        transform: rotate(0deg);
    }
    25% {
        transform: rotate(5deg);
    }
    50% {
        transform: rotate(0deg);
    }
    75% {
        transform: rotate(-5deg);
    }
    100% {
        transform: rotate(0deg);
    }
    }
  </style>
