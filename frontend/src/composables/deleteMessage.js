import axios from "axios";

export default async function deleteMessage(id) {
    let url = `/api/message/${id}/`;
    await axios.delete(url);

}