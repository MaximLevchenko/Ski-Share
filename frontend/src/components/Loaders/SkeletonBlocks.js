import ContentLoader from 'react-content-loader'


const SkeletonBlocks = (props) => (
  <ContentLoader
    speed={2}
    width={600}
    height={400}
    viewBox='0 0 800 400'
    backgroundColor='#f3f3f3'
    foregroundColor='#ecebeb'
    {...props}
  >
    <rect x='4' y='-4' rx='3' ry='3' width='223' height='332' />
    <rect x='265' y='-8' rx='3' ry='3' width='223' height='332' />
    <rect x='522' y='-9' rx='3' ry='3' width='223' height='332' />
  </ContentLoader>
)

export default SkeletonBlocks
