export default function getFullResponseFromAPI(success) {
  if (success === true) {
    return Promise.resolve({
      status: 200,
      body: 'Success',
    });
  }
  throw new Error('the fake APi is not working currently');
}
