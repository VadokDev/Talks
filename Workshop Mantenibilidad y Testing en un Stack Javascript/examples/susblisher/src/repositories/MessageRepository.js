const MessageRepository = ({ HttpClient }) => {
  const httpClient = HttpClient;

  const getMessages = async () => {
    const messages = await httpClient.get('/messages');
    return messages.data;
  };

  const sendMessage = async (content) => {
    const mensaje = { content };
    await httpClient.post('/messages', mensaje);
    return 'ok';
  };

  return { getMessages, sendMessage };
};

export default MessageRepository;
