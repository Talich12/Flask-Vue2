<template> 
    <div class="center con-pagination" style="margin-top: 7vh;">
        <vs-pagination not-margin color="danger" progress v-model="page" :length="len" />
        <vs-select placeholder="Кол-во на странице" v-model="value">
        <vs-option label="4" value="4">
          4
        </vs-option>
        <vs-option label="6" value="6">
          6
        </vs-option>
        <vs-option label="8" value="8">
          8
        </vs-option>
        <vs-option label="10" value="10">
          10
        </vs-option>
        <vs-option label="12" value="12">
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
        },
        value: function(){
            this.$emit('value', {value: this.value})
        }
    }
}   

</script>

<style>
button{
    font-family: 'Unbounded';
}
</style>