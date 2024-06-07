<script setup>
//as props definem as informações que VEM de fora para dentro do componente
const props = defineProps({
    label: {type: String, required: true},
    type: {type: String, default: 'text'},
    inputId: {type: String, required: true, default: 'custom_input'}
});
//o model vai definir a informação que VAI PARA fora do componente
const model = defineModel();
</script>

<template>
    <div class="custom_input_field">
        <label :for="props.inputId">{{ props.label }}</label>
        <input v-model="model" :id="props.inputId" :type="props.type">
    </div>
</template>

<style scoped lang="scss">
.custom_input_field {
    overflow-y: hidden;
    label{
        width: 100%;
        color: black;
        font-weight: bold;
        transition: 0.3s;
    }    
   
    input{
        width:100%;
        padding:10px;
        border: 0;
        border-bottom: solid black;
        font-size:20px;
        transition: 0.3s;
        &:focus{
            outline: 0;
            border-color: rgb(144, 0, 255);
        }
    }
}
</style>