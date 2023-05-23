<template>
      <vs-card-group style="margin-left: 8%; margin-top: 2%;">
    <vs-card v-for="post in Data">
      <template #title>
        <h3>Демо</h3>
      </template>
      <template #img>
        <img :src="require(`@/assets/img/load/${post.img}`)" alt="">
      </template>
      <template #text>
        <p>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit.
        </p>
      </template>
      <template #interactions>
        <vs-button danger icon>
          <i class='bx bx-heart'></i>
        </vs-button>
        <vs-button class="btn-chat" shadow primary>
          <i class='bx bx-chat' ></i>
          <span class="span">
            54
          </span>
        </vs-button>
      </template>
    </vs-card>
  </vs-card-group>
</template>

<script>

</script>