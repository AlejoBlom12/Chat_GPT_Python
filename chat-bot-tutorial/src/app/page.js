"use client"
import {useState} from 'react'

function HomePage(){

  const [prompt, setPrompt] = useState('')

  const onSubmit = async(e) => {
    e.preventDefault()
    
    const response = await fetch('/api/generate', {
      method: 'POST',
      headers: {
        'content-Type': 'application/json'
      },
      body: JSON.stringify({prompt})
    })
    const date = await response.json();
    console.log (data)
  };

  return(

    <div className='bg-zinc-950 h-screen flex justify-center items-center'>
      <form onSubmit={onSubmit}>
        <input type="text"
          placeholder='Ingresa tu consulta'
          onChange={e => setPrompt(e.target.value)}
          className='p-2 block bg-neutral-700 text-white 2-full rounded-md'
        />
        <button className='bg-green-500 p-2 rounded-md block mt-2 text-white'>
          Generate
        </button>
      </form>

    </div>
  )
}

export default HomePage