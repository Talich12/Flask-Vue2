<template>
    <div class="cookie">
    <vs-button
        upload
        color="danger"
        transparent
        :active="active == 5"
        @click="active = 5"
        style="width: 45%;"
      >
        Согласен
      </vs-button>
      <vs-button
        color="rgb(210, 61, 61)"
        default
        :active="active == 5"
        @click="active = 5"
        style="width: 45%;"
      >
        Не согласен
      </vs-button>
      </div>
</template>

<script>
export default {
  data:() => ({
    active: 0
  })
}
</script>

<style>
.cookie {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content:baseline;
}
</style>