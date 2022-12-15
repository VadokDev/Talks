import { render, fireEvent, screen } from '@testing-library/react';
import App from '../../App';
import nock from 'nock';

test('Should publish a message successfully', async () => {
  render(<App />);
  const baseURL = 'http://localhost:8000';
  const testMessage = 'Prueba Mock';
  const mockResponse = [{ content: testMessage }];
  const corsHeaders = {
    'Access-Control-Allow-Methods':
      'PUT, OPTIONS, CONNECT, PATCH, GET, HEAD, POST, DELETE, TRACE',
    'Access-Control-Allow-Origin': 'http://localhost',
    'Access-Control-Expose-Headers': 'link, etag, location',
    'Access-Control-Allow-Headers': 'user-agent',
  };

  nock(baseURL).options('/messages').reply(200, null, corsHeaders);
  nock(baseURL).post('/messages').reply(200, null, corsHeaders);
  nock(baseURL).options('/messages').reply(200, null, corsHeaders);
  nock(baseURL).get('/messages').reply(200, mockResponse, corsHeaders);

  const firstMessageButton = screen.getAllByRole('button')[0];
  await fireEvent.click(firstMessageButton);
  const expectedMessage = await screen.findByText(testMessage);

  expect(expectedMessage).toBeInTheDocument();
});
