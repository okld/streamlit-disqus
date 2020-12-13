import React from "react"
import { ComponentProps, Streamlit, withStreamlitConnection } from "streamlit-component-lib"
import { DiscussionEmbed } from "disqus-react"

import HeightObserver from "./height-observer"

const StreamlitPlayer = ({ args }: ComponentProps) => {
  return (
    <HeightObserver onChange={Streamlit.setFrameHeight}>
      <DiscussionEmbed
        shortname={args.shortname}
        config={{
          url: args.url || undefined,
          identifier: args.identifier || undefined,
          title: args.title || undefined,
          categoryID: args.categoryID || undefined,
          language: args.language || undefined
        }}
      />
    </HeightObserver>
  )
}

export default withStreamlitConnection(StreamlitPlayer)
