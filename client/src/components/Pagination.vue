<template> 
    <div class="center con-pagination page" style="margin-top: 7vh; display: flex; flex-direction: column; width: 100%;">
        <vs-pagination not-margin color="danger" progress v-model="page" :length="len" style=""/>
        <vs-select placeholder="Кол-во на странице" v-model="value" style="min-width: 8vw; max-width: 8vw; justify-content: center; align-content: center; margin: 0 auto; margin-top: 2vh;">
        <template #message-success>
          На странице
        </template>
        <vs-option label="4 поста" value="4">
          4
        </vs-option>
        <vs-option label="6 постов" value="6">
          6
        </vs-option>
        <vs-option label="8 постов" value="8">
          8
        </vs-option>
        <vs-option label="10 постов" value="10">
          10
        </vs-option>
        <vs-option label="12 постов" value="12">
          12
        </vs-option>
      </vs-select>
    </div>
</template>

<script>
export default {
    props: ['len', 'page'],
    data:() => ({
      value: '4',
    }),
    watch: {
        page: function(){
            this.$emit('page', {page: this.page})
            this.openLoading();
        },
        value: function(){
            this.$emit('value', {value: this.value})
            this.openLoading();
        }
    },
    methods: {
      openLoading() {
        const loading = this.$vs.loading({
          background: 'dark',
          color: 'danger',
          type: 'points'
        });
        setTimeout(() => {
          loading.close();
        }, 600);
      },
    }
}   

</script>

<style>
button {
    font-family: 'Unbounded';
    color: rgb(106, 78, 147);
}

input { 
  font-family: 'Unbounded';
}
</style>