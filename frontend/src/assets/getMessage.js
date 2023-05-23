import axios from 'axios';

const getMessage = async (messageId) => {
    try {
        const response = await axios.get(`http://backend:8000/messages/${messageId}`);
        return response.data;
    } catch (error) {
        console.error(error);
    }
};

export default getMessage;