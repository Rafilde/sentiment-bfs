import axios from 'axios';
import { toast } from 'react-toastify';

export const validateFile = (file) => {
    if (file && file.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') {
        return true;
    }
    return false;
};

export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
        await axios.post('http://127.0.0.1:5000/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return { success: true };
    } catch (error) {
        console.error('Erro ao enviar o arquivo:', error);
        return { success: false, error: 'Erro ao enviar o arquivo.' };
    }
};

export const notifySuccess = (message) => {
    toast.success(message);
};

export const notifyError = (message) => {
    toast.error(message);
};
