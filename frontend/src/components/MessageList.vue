<template>

    <div v-for="message in info.results" v-bind:key="message.url" id="message">
        <div class="grid">
            <div>
                <div class="a-title-container">
                    {{ message.title }}
                </div>
                <div class="body-container">
                    {{ message.body }}
                </div>
                <div>{{ formatted_time(message.created) }}</div>
                <div class="delete-message" @click="deleteMsg(message.id)">Delete</div>
            </div>
        </div>
    </div>


    <div id="paginator">
        <span v-if="is_page_exists('previous')">
            <router-link :to="get_path('previous')">
                Prev
            </router-link>
        </span>
        <span class="current-page">
            {{ get_page_param('current') }}
        </span>
        <span v-if="is_page_exists('next')">
            <router-link :to="get_path('next')">
                Next
            </router-link>
        </span>
    </div>

</template>

<script>
    import {ref} from 'vue'
    import {useRoute, useRouter} from 'vue-router'
    import getMessageData from '@/composables/getMessageData'
    import pagination from '@/composables/pagination'
    import formattedTime from '@/composables/formattedTime'
    import deleteMessage from '@/composables/deleteMessage'

    export default {
        name: 'MessageList',

        setup() {
            const info = ref('');
            const route = useRoute();
            const router = useRouter();

            const kwargs = ref({page: 0});

            getMessageData(info, route, kwargs);

            const {
                is_page_exists,
                get_page_param,
                get_path
            } = pagination(info, route);

            const formatted_time = formattedTime;

            const deleteMsg = async (id) => {
                let text = "Are you sure?";
                if (confirm(text) == true) {
                    await deleteMessage(id);
                    router.go(0);
                }
            }

            return {
                info,
                is_page_exists,
                get_page_param,
                get_path,
                formatted_time,
                deleteMsg,
            }
        },
    }

</script>

<style scoped>

    .grid {
        padding: 10px;
        background-color: #eee;
        position: relative;
    }

    #message {
        padding: 10px;
        margin: auto;
        max-width: 1020px;
    }
    .a-title-container {
        padding: 5px 0 5px 0;
        font-weight: bold;
    }

    .body-container{
        padding: 15px 0 5px 0;
    }

    #paginator {
        text-align: center;
        padding-top: 50px;
    }

    a {
        color: black;
    }

    .current-page {
        font-size: x-large;
        font-weight: bold;
        padding-left: 10px;
        padding-right: 10px;
    }

    .delete-message {
        position: absolute;
        bottom: 5px;
        right: 5px;
        cursor: pointer;
    }
    .delete-message:hover {
        color: red;
    }

</style>
