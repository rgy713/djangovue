import axios from 'axios';
import {onMounted, watch} from 'vue'

export default function getMessageData(info, route, kwargs) {
    const getData = async () => {

        const queryPage = route.query.page !== undefined ? parseInt(route.query.page) : 1;
        if (kwargs.value.page === queryPage) {
            return
        }

        let url = '/api/message';

        let params = new URLSearchParams();
        let userId = localStorage.getItem('userId.myblog');

        params.appendIfExists('page', route.query.page);
        params.appendIfExists('user_id', userId);

        const paramsString = params.toString();
        if (paramsString.charAt(0) !== '') {
            url += '/?' + paramsString
        }

        const response = await axios.get(url);


        info.value = response.data;
        kwargs.value.page = queryPage;
    };

    onMounted(getData);

    watch(route, getData);
}