<template> 
    <div class="center con-pagination" style="margin-top: 7vh;">
        <vs-pagination not-margin color="danger" progress v-model="page" :length="20" />
    </div>
</template>

<script>
export default {
    data:() => ({
        page: 1,
    }),
}
</script>

<style>
button{
    font-family: 'Unbounded';
}
</style>