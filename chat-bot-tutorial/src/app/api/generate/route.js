import { NextResponse } from "next/server"

export function POST(resquest){
    return NextResponse.json({message: 'hello world from api'})
}
