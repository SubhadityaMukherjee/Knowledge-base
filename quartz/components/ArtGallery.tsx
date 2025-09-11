import { QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

// Import art data from JSON file
import artData from "../../content/art-data.json"

interface ArtImage {
  src: string
  alt: string
  title?: string
}

const artImages: ArtImage[] = artData as ArtImage[]

function ArtGallery({ displayClass }: QuartzComponentProps) {
  return (
    <div className={classNames(displayClass, "art-gallery")}>
      {artImages.length === 0 ? (
        <div className="art-gallery-empty">
          <p>No art images found. Please check your art-data.json file.</p>
        </div>
      ) : (
        <div className="art-gallery-grid">
          {artImages.map((image, index) => (
            <div key={index} className="art-gallery-item" onClick={() => window.open(image.src, '_blank')}>
              <div className="art-gallery-image-container">
                <img
                  src={image.src}
                  alt={image.alt}
                  title={`${image.title}`}
                  loading="lazy"
                  className="art-gallery-image"
                />
                <div className="art-gallery-overlay">
                  <div className="art-gallery-title">{image.title}</div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default (() => ArtGallery) satisfies QuartzComponentConstructor
