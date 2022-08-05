<template>

    <BlogHeader/>

    <div class="selete-tab">
        <label><input v-model="isSend" type="radio" name="send-receive" value="0"/> Sent messages</label>
        <label><input v-model="isSend" type="radio" name="send-receive" value="1"/> Received messages</label>
    </div>

    <div class="right-div">
        <span @click="newMessage">New Message</span>
    </div>

    <MessageList v-if="isSend==0"></MessageList>

    <ReceivedMessageList v-else-if="isSend==1"></ReceivedMessageList>

    <BlogFooter/>

</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import MessageList from '@/components/MessageList.vue'
    import ReceivedMessageList from '@/components/ReceivedMessageList.vue'

    export default {
        name: 'Home',
        components: {BlogHeader, BlogFooter, MessageList, ReceivedMessageList},
        data(){
            return {
                isSend: 0,
            }
        },
        methods: {
            newMessage(){
                this.$router.push({name: 'SendMessage'})
            }
        }
    }
</script>

<style scoped>

    .selete-tab {
        display: flex;
        justify-content: center;
    }
    .right-div{
        text-align: right;
    }
    .right-div span {
        cursor: pointer;
    }
</style>