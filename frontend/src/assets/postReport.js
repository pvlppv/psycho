import axios from 'axios';

const postReport = async(message_id, report_text) => {
    try {
        const response = await axios.post(`http://localhost:8000/report/post`, {message_id, report_text});
        return response.data;
    } catch(error) {
        console.log(error)
    }
};

export default postReport;