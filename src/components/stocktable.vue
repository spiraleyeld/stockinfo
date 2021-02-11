<template>
    <h2 class="blue">Stock Good Info {{ msg }}</h2>
</template>
<script>
export default {
    name:'StockGoodNews',
    props:{
        msg:{
            type:String,
            default: "ALL in Here !!!"
        }
    },
    methods:{
    },
    data(){
        return{
        }
    },
}
</script>
<style>
.blue {
    color:skyblue;
}
</style>