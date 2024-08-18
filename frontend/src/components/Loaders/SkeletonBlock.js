import ContentLoader from "react-content-loader"


const SkeletonBlock = (props) => (
  <ContentLoader 
    speed={2}
    width={860}
    height={350}
    viewBox="0 0 860 350"
    backgroundColor="#f3f3f3"
    foregroundColor="#ecebeb"
    {...props}
  >
    <rect x="0" y="0" rx="3" ry="3" width="860" height="350" />
  </ContentLoader>
)

export default SkeletonBlock