import React, { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import axios from 'axios';

const Home = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [dragActive, setDragActive] = useState(false);
    const inputRef = useRef(null);
    const navigate = useNavigate();

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file && file.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') {
            setSelectedFile(file);
            toast.success('Arquivo selecionado com sucesso!')
        } else {
            setSelectedFile(null);
            toast.error('Arquivo em formato incompatível!');
        }
    };

    const handleDragOver = (event) => {
        event.preventDefault();
        event.stopPropagation();
        setDragActive(true);
    };

    const handleDragLeave = (event) => {
        event.preventDefault();
        event.stopPropagation();
        setDragActive(false);
    };

    const handleDrop = (event) => {
        event.preventDefault();
        event.stopPropagation();
        setDragActive(false);
    
        if (event.dataTransfer.files && event.dataTransfer.files[0]) {
            const file = event.dataTransfer.files[0];
            console.log('Tipo de arquivo:', file.type);  
            if (file.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') {
                setSelectedFile(file);
                toast.success('Arquivo selecionado com sucesso!')
            } else {
                setSelectedFile(null);
                toast.error('Arraste apenas um arquivo no formato XLSX.');
            }
        }
    };
    
    const handleButtonClick = () => {
        inputRef.current.click();
    };

    const handleContinueClick = async () => {
        if (selectedFile) {
            const formData = new FormData();
            formData.append('file', selectedFile);

            try {
                await axios.post('http://127.0.0.1:5000/upload', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });
                navigate('/dashboard');
            } catch (error) {
                // console.error('Erro ao enviar o arquivo:', error);
                toast.error('Erro ao enviar o arquivo.');
            }
        } else {
            toast.error('Nehum arquivo selecionado.')
        }
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen p-4 relative overflow-hidden bg-backgroundcolor">
            <div className="absolute top-[-50px] left-[-50px] w-64 h-64 bg-primary rounded-full opacity-30 animate-bounce-slow"></div>
            <div className="absolute bottom-[-70px] right-[-70px] w-96 h-96 bg-secondary rounded-full opacity-40 animate-pulse-slow"></div>
            <ToastContainer position='bottom-right' autoClose={4000}  />
            <div className="max-w-lg w-full bg-white shadow-lg rounded-lg p-8 relative z-10">
                <h1 className="text-4xl font-bold text-center text-accent mb-4">
                    Distâncias entre Locais
                </h1>

                <p className="text-center text-textcolor mb-6">
                    Faça o upload de um arquivo XLSX contendo informações de locais e as distâncias entre eles.
                </p>

                <div
                    className={`border-4 ${
                        dragActive ? 'border-primary bg-yellow-100' : 'border-secondary'
                    } border-dashed rounded-lg p-10 flex flex-col items-center justify-center transition-all duration-300 ease-in-out`}
                    onDragOver={handleDragOver}
                    onDragLeave={handleDragLeave}
                    onDrop={handleDrop}
                >
                    <input
                        type="file"
                        ref={inputRef}
                        accept=".xlsx"
                        onChange={handleFileChange}
                        className="hidden"
                    />

                    <button
                        onClick={handleButtonClick}
                        className="bg-accent text-white font-bold py-2 px-6 rounded-lg mb-4 hover:bg-primary shadow-md transition-all duration-300 ease-in-out transform hover:scale-105 active:scale-95"
                    >
                        Faça Upload
                    </button>

                    <p className="text-textcolor text-center">ou arraste um arquivo XLSX aqui</p>
                </div>

                {selectedFile && (
                    <div className="mt-6 text-center">
                        <p className="text-textcolor font-medium">
                            Arquivo selecionado: <span className="text-accent">{selectedFile.name}</span>
                        </p>
                    </div>
                )}

                <div className="flex justify-center mt-8">
                    <button
                        onClick={handleContinueClick}
                        disabled={!selectedFile}
                        className={`py-3 px-8 font-bold rounded-lg transition-all duration-300 ease-in-out transform ${
                            selectedFile
                                ? 'bg-primary text-white hover:bg-secondary shadow-lg hover:scale-105 active:scale-95'
                                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
                        }`}
                    >
                        Continuar
                    </button>
                </div>
            </div>
        </div>
    );
};

export default Home;
