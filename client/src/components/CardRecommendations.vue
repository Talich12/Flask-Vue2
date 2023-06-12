<template>
      <vs-card-group style="margin-left: 8%; margin-top: 2%;">
        <div v-for="post in $props.data">
          <card @data="Open" :post="post">
        </card>
        </div>
  </vs-card-group>
</template>

<script>
export default {
  props:['data'],
  data() {
      return {
      
      };
  },
  methods:{
    Open(data){
      this.$emit('data', data)
    }
  }
}
</script>