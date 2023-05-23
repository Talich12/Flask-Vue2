<template> 
    <div class="center con-pagination" style="margin-top: 7vh;">
        <vs-pagination not-margin color="danger" progress v-model="page" :length="len" />
    </div>
</template>

<script>
export default {
    props: ['len'],
    data:() => ({
        page: 1,
    }),
    watch: {
        page: function(){
            this.$emit('page', {page: this.page})
        }
    }
}   

</script>

<style>
button{
    font-family: 'Unbounded';
}
</style>