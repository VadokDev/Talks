import axios from 'axios';
import MessageRepository from './MessageRepository';

const HttpClient = axios.create({ baseURL: 'http://localhost:8000' });
const messageRepository = MessageRepository({ HttpClient });

export { messageRepository };
