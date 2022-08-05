<template>
    <BlogHeader/>
    <div id="message-create">
        <h3>New Message</h3>

        <form>
            <div class="form-elem">
                <span>Title：</span>
                <input v-model="title" type="text" placeholder="Enter title">
            </div>

            <div class="form-elem">
                <label>Recipient：
                    <select v-model="selecdtedUser">
                        <option
                            v-for="user in users"
                            :key="user.id"
                            :value="user.id"
                        >
                            {{user.username}}
                        </option>
                    </select>
                </label>
            </div>

            <div class="form-elem">
                <label>Content：
                    <textarea v-model="body" placeholder="Enter content" rows="20"></textarea>
                </label>
            </div>

            <div class="form-elem">
                <button v-on:click.prevent="submit">Send</button>
            </div>
        </form>
    </div>
    <BlogFooter/>
</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import axios from 'axios';
    import authorization from '@/utils/authorization';

    export default {
        name: 'ArticleCreate',
        components: {BlogHeader, BlogFooter},
        data: function () {
            return {
                title: '',
                body: '',
                users: [],
                selecdtedUser: null,
            }
        },
        mounted() {
            axios
                .get('/api/user/')
                .then(response => this.users = response.data.results)
        },
        methods: {
            submit() {
                const that = this;
                authorization()
                    .then(function (response) {
                            if (response[0]) {
                                if(!that.title) {
                                    alert('Please enter title')
                                    return false;
                                }
                                if(!that.selecdtedUser) {
                                    alert('Please recipient title')
                                    return false;
                                }
                                if(!that.body) {
                                    alert('Please enter content')
                                    return false;
                                }
                                let data = {
                                    title: that.title,
                                    body: that.body,
                                    recipient_id: that.selecdtedUser,
                                    sender_id: response[2]
                                };

                                const token = localStorage.getItem('access.myblog');
                                axios
                                    .post('/api/message/',
                                        data,
                                        {
                                            headers: {Authorization: 'Bearer ' + token}
                                        })
                                    .then(function (response) {
                                        console.log(response);
                                        that.$router.push({name: 'Home'});
                                    })
                            }
                            else {
                                alert('Token expired. Please login again.')
                            }
                        }
                    )
            }
        }
    }
</script>

<style scoped>

    .category-btn {
        margin-right: 10px;
    }

    #message-create {
        text-align: center;
        font-size: large;
        max-width: 1020px;
        margin: auto;
    }

    form {
        text-align: left;
        padding-left: 100px;
        padding-right: 10px;
    }

    .form-elem {
        padding: 10px;
    }
    select {
        padding: 5px;
    }
    input, textarea {
        height: 25px;
        padding: 10px;
        width: 100%;
        font-size: 16px;
    }

    textarea {
        height: 300px;
    }

    button {
        height: 35px;
        cursor: pointer;
        border: none;
        outline: none;
        background: steelblue;
        color: whitesmoke;
        border-radius: 5px;
        width: 150px;
        padding: 5px;
        font-size: 16px;
    }
</style>